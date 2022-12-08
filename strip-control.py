#!/usr/bin/env python3

import time
from rpi_ws281x import PixelStrip, Color
import argparse

# LED strip configuration:
LED_COUNT = 300       # Number of LED pixels.
LED_PIN = 21          # PCM data out
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

def colorWipe(strip, color, wait_ms=50):
  for i in range(strip.numPixels()):
    strip.setPixelColor(i, color)
    strip.show()
    time.sleep(wait_ms / 1000.0)

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


def rainbow(strip, wait_ms=20, iterations=1):
  """Draw rainbow that fades across all pixels at once."""
  for j in range(256 * iterations):
    for i in range(strip.numPixels()):
      strip.setPixelColor(i, wheel((i + j) & 255))
    strip.show()
    time.sleep(wait_ms / 1000.0)

if __name__ == '__main__':
  # Process arguments
  parser = argparse.ArgumentParser()
  parser.add_argument('-m', '--mode', required=True, help='select mode to display on LED strip')
  parser.add_argument('-r', '--red', type=int, default=255, help='red color')
  parser.add_argument('-g', '--green', type=int, default=255, help='green color')
  parser.add_argument('-b', '--blue', type=int, default=255, help='blue color')
  parser.add_argument('-B', '--brightness', type=int, default=255, help='change brightness')
  parser.add_argument('-s', '--speed', type=int, default=10, help='change speed of animation')
  args = parser.parse_args()
  print(args);
  # Create NeoPixel object with appropriate configuration.
  strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  # Intialize the library (must be called once before other functions).
  strip.begin()

  try:
    if args.mode == "color":
      colorWipe(strip, Color(args.red, args.green, args.blue), 10)
    elif args.mode == "rainbow":
      while True:
        rainbow(strip);
    else:
      print(f"Error: no {args.mode} mode found")
  except KeyboardInterrupt:
      colorWipe(strip, Color(0, 0, 0), 10)
