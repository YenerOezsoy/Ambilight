#import bibliopixel
import os
import sys

from bibliopixel import *
from bibliopixel.animation import StripChannelTest
from bibliopixel.drivers.LPD8806 import *

from flask import Flask, render_template, redirect, url_for,request
from flask import make_response
app = Flask(__name__)

global farbe

@app.route("/")
def home():
    return "hi"

@app.route("/helligkeit", methods=['GET', 'POST'])
def helligkeit():
    driver = DriverLPD8806(116)
    value = int(request.form['brightness'])
    value = (value * 255) / 100
    value = int(value)
    print value
    led = LEDStrip(driver,masterBrightness = value)
    led.fillRGB(farbe[2], farbe[0], farbe[1])
    led.update()
    return "changed brightness"

@app.route("/farbe", methods=['GET', 'POST'])
def farbe():
    value = request.form['color']
    global farbe
    farbe = stringToHex(value)
    led.fillRGB(farbe[2], farbe[0], farbe[1])
    led.update()
    return "changed color"

@app.route("/ambi", methods=['GET', 'POST'])
def ambi():
    value = request.form['status']
    print(value)
    if (value == 'true'):
        os.system("sudo service hyperion start")
    else:
        os.system("sudo service hyperion stop")
    return "toggled ambi"

def stringToHex(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv / 3], 16) for i in range(0, lv, lv / 3))

def init():
    global helligkeit
    helligkeit = 255
    global farbe
    farbe = stringToHex("#ffffff")
    global driver
    driver = DriverLPD8806(116)
    global led
    led = LEDStrip(driver, masterBrightness=helligkeit)

    led.fillRGB(farbe[2], farbe[0], farbe[1])
    led.update()


if __name__ == "__main__":
    init()
    app.run(host='0.0.0.0')
#if __name__ == '__main__':
 #   init()
  #  if sys.argv[1] == 1:
#	farbe = stringToHex("#123456")
#	led.fillRGB(farbe[0], farbe[1], farbe[2])
    #app.run(host='0.0.0.0', port=port)
