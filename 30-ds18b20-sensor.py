import time
from w1thermsensor import W1ThermSensor
sensor = W1ThermSensor()
while 1:
    temp_c = sensor.get_temperature()
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    print "-------------------------------"
    print temp_c
    print temp_f
    print "-------------------------------"
    print "the temperature in celcius is = %0.2f *C" %temp_c
    print "the temperature in Fahrenheit is = %0.2f *F" %temp_f
    time.sleep(0.3)
    