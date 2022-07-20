import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.IN)
while 1:
	if GPIO.input(24)==0:
		GPIO.output(17,1)
		GPIO.output(27,1)
		GPIO.output(22,1)
		print "Input Low  hai and button pressed hai  :)"
	else:
		GPIO.output(17,1)
		GPIO.output(27,0)
		GPIO.output(22,1)
		print "input high  hai :) "
	time.sleep(0.3)