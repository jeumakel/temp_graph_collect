from pymongo import MongoClient
from Adafruit_I2C import Adafruit_I2C
import os
import time

#set the device addresss
data = Adafruit_I2C(0x4b)
degree_sign = u'\N{DEGREE SIGN}'

def getIndoorTemperature():
	#set the address
	datalist = data.readList(0x00, 2)
	#print bin((datalist[0]<<8)|datalist[1])
	# get the MSB and LSB and calculate the temp
	temp = (datalist[0]<<8)|datalist[1]
	tempraw = (temp>>3)*0.0625
	return tempraw

def getOutdoorTemperature():
	return 10;

def storeTemperature(key):
	try:
		if key == "temp_in":
			temp = getIndoorTemperature()
			db.temperatures.save({"temp_in": temp})
		elif key == "temp_out":
			temp = getOutdoorTemperature()
			db.temperatures.save({"temp_out": temp})
		else:
			raise NameError("Unknown temperature key error")
		print(key + ": %.1f" % round(temp, 1) + degree_sign + "C")
	except (Exception) as e:
		print(repr(e))

client = MongoClient()
try:
	while(True):
		db = client["temp_db"]
		storeTemperature("temp_in")
		storeTemperature("temp_out")
		time.sleep(60 * 5)
except KeyboardInterrupt:
	print(' received, exiting')
	client.close();
	exit()

except (Exception) as e:
	print(repr(e))
	client.close()
	exit()

