## Demos for the Adafruit Voice Bonnet

### Purpose

Demonstrates controlling the features of the [Adafruit Voice Bonnet](https://learn.adafruit.com/adafruit-voice-bonnet?view=all) from within Docker containers. 
Each feature is controlled independently to confirm they can be used without interfering with each other.

Features demonstrated by each container:
* `rainbow` - controls the three DotStar LEDs
* `oled-hello` - controls a 128x32 pixel OLED display connected to the I2C STEMMA port
* `white-noise` - controls a speaker connected to the speaker port

### Tested Hardware

* [Raspberry Pi Zero W Rev1.1](https://www.raspberrypi.com/products/raspberry-pi-zero-w/)
* [Adafruit Voice Bonnet](https://www.adafruit.com/product/4757)
* [Adafruit OLED, Monochrome 128x32](https://www.adafruit.com/product/4440)
* [Adafruit Mono Speaker, 3W 4 Ohm](https://www.adafruit.com/product/3351)

### Prerequisites

* Install Raspberry Pi OS Lite to an SD Card (out-of-scope for this doc)
* Setup WiFi or connect a monitor and keyboard (out-of-scope for this doc)
* Install Docker & Docker Compose (TBD)
* For the OLED demo, enable I2C support: `sudo raspi-config nonint do_i2c 0`
* For the speaker demo, [install the seeed-voicecard](https://learn.adafruit.com/adafruit-voice-bonnet/audio-setup)

### Usage

On the Raspberry Pi:
* `git clone https://github.com/jaxzin/adafruit-voice-docker`
* `cd adafruit-voice-docker`
* `docker-compose up -d`

If all the prerequisites are satisfied and precreated Docker images can be downloaded, then after about 30 seconds the following will happen:
* The three DotStar LEDs will glow with a changing rainbow pattern
* The OLED will display "Hello World" with a border
* The speaker will play white-noise

To make it stop:
* `docker-compose stop`

To tear it all down:
* `docker-compose down`

Each of these demos runs within a separate docker container independently.
