#!/usr/bin/env python




import time
import Netmaxiot

# Connect the Netmaxiot LED to digital port D4
led1 = 4
led2 = 3
Netmaxiot.pinMode(led1,"OUTPUT")
Netmaxiot.pinMode(led2,"OUTPUT")
time.sleep(1)
print "starts now "
while True:
    Netmaxiot.digitalWrite(led1,1)		# Send HIGH to switch on LED
    print ("LED ON!-----:)")
    time.sleep(1)
    Netmaxiot.digitalWrite(led1,0)		# Send LOW to switch off LED
    print ("LED OFF!------:(")
    time.sleep(1)

