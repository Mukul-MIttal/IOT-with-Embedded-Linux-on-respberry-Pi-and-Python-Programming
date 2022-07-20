#!/usr/bin/env python
import time
import Netmaxiot
# Connect the Netmaxiot LED to digital port D4
led1 = 4
led2 = 3
led3 = 2
button1 = 8
button2 = 9
Netmaxiot.pinMode(button1,"INPUT")
Netmaxiot.pinMode(button2,"INPUT")
Netmaxiot.pinMode(led1,"OUTPUT")
Netmaxiot.pinMode(led2,"OUTPUT")
Netmaxiot.pinMode(led3,"OUTPUT")
time.sleep(1)
print "starts now "
while True:
	try:
		a= Netmaxiot.digitalRead(button1)
		b= Netmaxiot.digitalRead(button2)
		if a==0:
			Netmaxiot.digitalWrite(led1,1)		# Send HIGH to switch on LED
			Netmaxiot.digitalWrite(led2,1)
			Netmaxiot.digitalWrite(led3,1)
			print ("button 1 pressed LED ON!-----:)")
			time.sleep(0.2)
			Netmaxiot.digitalWrite(led1,0)		# Send LOW to switch off LED
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,0)
			print ("button 1 pressed LED OFF!------:(")
			time.sleep(0.2)
		elif b==0:
			Netmaxiot.digitalWrite(led1,1)		# Send HIGH to switch on LED
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,1)
			print ("button 2 pressed LED ON!-----:)")
			time.sleep(0.2)
			Netmaxiot.digitalWrite(led1,0)		# Send LOW to switch off LED
			Netmaxiot.digitalWrite(led2,1)
			Netmaxiot.digitalWrite(led3,0)
			print ("button 2 pressed LED OFF!------:(")
			time.sleep(0.2)
		else :
			Netmaxiot.digitalWrite(led1,0)		# Send HIGH to switch on LED
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,1)
			print (" No button pressed LED ON!-----:)")
			time.sleep(0.2)
			Netmaxiot.digitalWrite(led1,1)		# Send LOW to switch off LED
			Netmaxiot.digitalWrite(led2,0)
			Netmaxiot.digitalWrite(led3,0)
			print ("No button pressed LED OFF!------:(")
			time.sleep(0.2)		
	except KeyboardInterrupt:
		Netmaxiot.digitalWrite(led1,0)
		Netmaxiot.digitalWrite(led2,0)
		Netmaxiot.digitalWrite(led3,0)
		print "you pressed Control + C byeeeee --:) "
		print "try except loop chal payi in Netmaxiot"
		break
	except IOError:
		print ("Error check shield Connections and power to shield")
    	
