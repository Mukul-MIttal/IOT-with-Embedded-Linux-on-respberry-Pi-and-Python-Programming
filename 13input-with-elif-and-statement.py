import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
###############################################
GPIO.setup(24,GPIO.IN)
GPIO.setup(23,GPIO.IN)
while 1:
	if GPIO.input(24)==0 and GPIO.input(23)==0 :
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
		time.sleep(0.4)
		GPIO.output(17,0)
		GPIO.output(27,0)
		GPIO.output(22,0)
		time.sleep(0.4)
		print " 24 and 23 Input Low  hai and button pressed hai  :)"
	elif GPIO.input(24)==1 and GPIO.input(23)==0:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,0)
		time.sleep(0.2)
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,1)
		time.sleep(0.2)
		print " 23 Input Low  hai and button pressed hai  :)"	
	else:
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		time.sleep(0.5)
		GPIO.output(17,0)
		GPIO.output(27,1)
		GPIO.output(22,0)
		time.sleep(0.5)
		print "input high  hai :) no button pressed "
	time.sleep(0.3)
