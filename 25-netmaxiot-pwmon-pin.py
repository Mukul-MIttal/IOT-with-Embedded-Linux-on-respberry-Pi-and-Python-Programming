#!/usr/bin/env python
import time
import Netmaxiot
xpin = 5
Netmaxiot.pinMode(xpin, "OUTPUT")
Netmaxiot.pinMode(6,"OUTPUT")
Netmaxiot.pinMode(7,"OUTPUT")
Netmaxiot.digitalWrite(5,0)		# Send LOW to switch off LED
Netmaxiot.digitalWrite(6,0)
Netmaxiot.digitalWrite(7,0)

#Netmaxiot.analogWrite(xpin,255)

while 1:
	Netmaxiot.analogWrite(xpin,255)
	print " pwm on pin 5 is full"
	time.sleep(2)
	Netmaxiot.analogWrite(xpin,128)
	print " pwm on pin 5 is half :)"
	time.sleep(2)
	Netmaxiot.analogWrite(xpin,75)
	print " pwm on pin 5 is 25 percent :)"
	time.sleep(2)
	Netmaxiot.analogWrite(xpin,25)
	print " pwm on pin 5 bahut low hai  :( "
	time.sleep(2)

