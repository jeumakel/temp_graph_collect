#FROM arm32v7/python:slim
FROM arm32v6/python:alpine3.7

WORKDIR /home/pi/projects/temp_graph_collect

#RUN apt-get update && apt-get install --no-install-recommends -y \
#	python3-pip && \ 
#	apt-get clean && \
#	pip3 install smbus2 && \
#	apt-get remove -y python3-pip  && \
#	rm -rf /var/lib/apt/lists/*

#RUN apk --update add --virtual .build-deps python3-pip \
#    && pip3 install --no-cache-dir smbus2 \
#    && apk del .build-deps \ 
#    && rm -rf ~/.cache 

RUN pip3 install --no-cache-dir smbus2 pymongo==3.5

COPY . .

CMD [ "python3", "./main.py" ]
