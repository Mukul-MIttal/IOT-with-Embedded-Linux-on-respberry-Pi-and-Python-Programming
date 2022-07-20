#!/usr/bin/python
import Adafruit_DHT

# Sensor should be set to Adafruit_DHT.DHT11,
# Adafruit_DHT.DHT22, or Adafruit_DHT.AM2302.

sensor = Adafruit_DHT.DHT11
pin = 18

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

if humidity is not None and temperature is not None:
	print "temp is = %0.2f *C and humidity is = %0.2f percent "%(temperature , humidity )

else:
	print('Failed to get reading. Try again! check sensor and connections on pi')

