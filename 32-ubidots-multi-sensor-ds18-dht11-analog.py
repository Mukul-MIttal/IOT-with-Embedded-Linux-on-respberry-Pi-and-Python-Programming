#!/usr/bin/python
#####################
import os
import time
import requests
from w1thermsensor import W1ThermSensor
import Adafruit_DHT
import Netmaxiot
#################################
sensor = W1ThermSensor()


def read_temp():
    #############################################
    valueread1 = Netmaxiot.analogRead(0)
    valueread2 = Netmaxiot.analogRead(1)
    voltage1 = valueread1 * 4.89#5000/1023
    temp=voltage1/10    # as 10mv=1c
    voltage2 = valueread2 * 4.89
    lightintensity = (voltage2/50)
    ##################################################3
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 18)
    #######################################################
    temp_c = sensor.get_temperature()
    temp_f = temp_c * 9.0 / 5.0 + 32.0
    ##############################################
    print "--------------------------"
    print "--------------------------"
    print "ds18b20 readings"
    print temp_c
    print temp_f
    print "--------------------------"
    print "dht11 readings"
    print humidity
    print temperature
    print "--------------------------"
    print "Analog Readings"
    print temp
    print lightintensity
    print "--------------------------"
    time.sleep(1)
    payload = {'temp_celsius': temp_c,'dht_temp': temperature,'dht_humidity': humidity,'temp_analog': temp,'Light Level': lightintensity}
    return payload

##################################################33

while True:
        try:
            r = requests.post('http://things.ubidots.com/api/v1.6/devices/raspberry/?token=A1E-YgEDtbiPKNxxEtSCp7nT8mJLMjxt2p', data=read_temp())
            print('Posting temperatures in Ubidots')
            print(read_temp())
        except:
                 
            time.sleep(10)

