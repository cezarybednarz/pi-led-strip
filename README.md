# pi-led-strip

## Access:
http://192.168.0.10/
http://chata.local/

## Build:
`sudo node server.js`

## LED strip configuration:
```
LED_COUNT = 300        # Number of LED pixels.
LED_PIN = 21
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA = 10          # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
```