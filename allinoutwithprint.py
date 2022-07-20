

import RPi.GPIO as GPIO
                                               
from time import sleep

GPIO.setwarnings(False)
print "all students of 4-6 batch today going late "

GPIO.setmode(GPIO.BOARD) ## Use board pin numbering

GPIO.setup(7,GPIO.OUT)
GPIO.setup(22,GPIO.IN)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

print "7 ,11,,13,15 are output , 22 is input."

while 1:
	if GPIO.input(22):
		GPIO.output(7, 1)
		GPIO.output(11,0)
		GPIO.output(13,1)
		GPIO.output(15,0)
		print "Switch is off :)"
		sleep(0.5)
	else:
		GPIO.output(7,1)
		GPIO.output(11,0)
		GPIO.output(15,True)
		print "Switch is ON"
		sleep(0.4)
