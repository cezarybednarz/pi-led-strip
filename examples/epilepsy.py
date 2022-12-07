#!/usr/bin/env python3
# NeoPixel library strandtest example
# Author: Tony DiCola (tony@tonydicola.com)
#
# Direct port of the Arduino NeoPixel library strandtest example.  Showcases
# various animations on a strip of NeoPixels.

import time
import random
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 300        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (18 uses PWM!).
# LED_PIN = 10        # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def drop(strip, color, wait_ms=50):
    for j in range(1000):
        r = random.randrange(0, strip.numPixels())
        delta = 0.01
        color = wheel(r)
        runup = 30
        while(delta < 0.5):
            strip.setPixelColor(r, color)
            if r >= strip.numPixels():
                continue
            strip.show()
            time.sleep(delta)
            if runup < 0:
                delta += 0.1
            else:
                runup -= 1
            strip.setPixelColor(r, Color(0, 0, 0)) 
            r = r+1

        
# Define functions which animate LEDs in various ways.
def waves(strip, color, wait_ms=50):
    for j in range(1000):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, color)
            strip.setPixelColor(i, color)
            strip.show()
            time.sleep(1.0/100.0)

def epilepsy(strip, color, wait_ms=50):
    for j in range(1000):
        for i in range(strip.numPixels()):
            strip.setPixelColor(color)
        for i in range(strip.numPixels()):
            strip.setPixelColor(Color(0,0,0))


def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)


# Main program logic follows:
if __name__ == '__main__':
    # Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    # Create NeoPixel object with appropriate configuration.
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    # Intialize the library (must be called once before other functions).
    strip.begin()

    print('Press Ctrl-C to quit.')
    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

    try:

        while True:
            print('Color wipe animations.')
            epilepsy(strip, Color(255, 255, 255), 50)

    except KeyboardInterrupt:
        if args.clear:
            colorWipe(strip, Color(0, 0, 0), 10)
