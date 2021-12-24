#FROM arm32v6/python:3-alpine
FROM arm32v5/python:3
#FROM woahbase/alpine-rpigpio:armhf

# Blinka setup
RUN pip3 install --upgrade adafruit-python-shell
RUN apt-get update -y
RUN apt-get install -y i2c-tools gcc
RUN apt-get install -y libc-dev
RUN CFLAGS=-fcommon pip3 install --no-cache-dir RPi.GPIO
RUN pip3 install --upgrade adafruit-blinka

RUN pip3 install --upgrade adafruit-circuitpython-dotstar adafruit-circuitpython-motor adafruit-circuitpython-bmp280

# Voice Bonnet setup
#RUN apt-get install -y git
#RUN git clone https://github.com/HinTak/seeed-voicecard
#RUN seeed-voicecard/install.sh

COPY rainbow.py .
ENTRYPOINT ["python", "rainbow.py"]
