#!/usr/bin/env python
import time
import Netmaxiot
# Connect the Netmaxiot LED to digital port D4
led1 = 4
led2 = 3
led3 = 2
Netmaxiot.pinMode(led1,"OUTPUT")
Netmaxiot.pinMode(led2,"OUTPUT")
Netmaxiot.pinMode(led3,"OUTPUT")
time.sleep(1)
print "starts now "
while True:
	try:
		Netmaxiot.digitalWrite(led1,1)		# Send HIGH to switch on LED
		Netmaxiot.digitalWrite(led2,1)
		Netmaxiot.digitalWrite(led3,1)
		print ("LED ON!-----:)")
		time.sleep(1)
		Netmaxiot.digitalWrite(led1,0)		# Send LOW to switch off LED
		Netmaxiot.digitalWrite(led2,0)
		Netmaxiot.digitalWrite(led3,0)
		print ("LED OFF!------:(")
		time.sleep(1)
	except KeyboardInterrupt:
		Netmaxiot.digitalWrite(led1,1)
		Netmaxiot.digitalWrite(led2,0)
		Netmaxiot.digitalWrite(led3,1)
		print "you pressed Control + C byeeeee --:) "
		print "try except loop chal payi in Netmaxiot"
		break
	except IOError:
		print ("Error check shield Connections and power to shield")
    	

