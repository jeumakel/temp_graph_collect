from pymongo import MongoClient
from Adafruit_I2C import Adafruit_I2C
import os
import time
#set the device addresss
data=Adafruit_I2C(0x4b)
degree_sign= u'\N{DEGREE SIGN}'
client=MongoClient()
try:
    while(True):
        db=client["temp_db"]
        #set the address
        datalist=data.readList(0x00,2)
        #print bin((datalist[0]<<8)|datalist[1])
        # get the MSB and LSB and calculate the temp 
        temp = (datalist[0]<<8)|datalist[1]
        tempraw =(temp>>3)*0.0625
        #print "the temperature at lab:"
#        print(tempraw)
        print("%.1f" % round(tempraw,1) + degree_sign + "C")
        db.temperatures.save({"temperature": tempraw})
        time.sleep(60 * 5)
except KeyboardInterrupt:
    print(' received, exiting')
    client.close();
    exit()

except (Exception) as e:
    print(repr(e))
    client.close()
    exit()
