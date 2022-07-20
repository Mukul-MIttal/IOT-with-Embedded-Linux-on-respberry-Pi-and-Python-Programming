import os
import time
import requests
from w1thermsensor import W1ThermSensor

#################################
sensor = W1ThermSensor()

def read_temp():
    temp_c = sensor.get_temperature()
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    print temp_c
    time.sleep(0.3)
    print temp_f
    payload = {'temp_celsius': temp_c, 'temp_fahrenheit': temp_f}
    return payload

##################################################33

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-oCih0lqgphnhyJwJsKqVIcaqPvf0FQ', data=read_temp())
            print('Posting temperatures in Ubidots')
            print(read_temp())
        except:
            print('Sada temperatures post nahin hoyaa in Ubidots check karo :( ')     
            time.sleep(10)

