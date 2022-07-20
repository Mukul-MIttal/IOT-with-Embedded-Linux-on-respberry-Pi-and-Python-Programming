import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) 
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.output(27,0)
GPIO.output(22,0)
GPIO.output(17,0)
########################
s = GPIO.PWM(17,1000) # 1 k hz 
s.start(90)

while 1:
	s.ChangeDutyCycle(90)
	print "duty cycles are 90 --"
	sleep(1)
	s.ChangeDutyCycle(70)
	print "duty cycles are 70 --"
	sleep(1)
	s.ChangeDutyCycle(50)
	print "duty cycles are 50 --"
	sleep(1)
	s.ChangeDutyCycle(30)
	print "duty cycles are 30 --"
	sleep(1)
	s.ChangeDutyCycle(10)
	print "duty cycles are 10 --"
	sleep(1)














