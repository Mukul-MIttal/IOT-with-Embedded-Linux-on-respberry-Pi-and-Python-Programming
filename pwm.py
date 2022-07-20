import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)

 GPIO.output(17,0)
GPIO.output(27,0)
GPIO.output(22,0)
s = GPIO.PWM(17,1000) #1KHZ
s.start(90)
a = GPIO.PWM(28,1000) #1KHZ
a.start(70)
b = GPIO.PWM(40,1000) #1KHZ
b.start(50)
while 1:
	s.ChangeDutyCycle(90)
	print " duty cycle of 17 is 90"
	sleep (1)
	a.ChangeDutyCycle(30)
	print "duty cycle of 28 is 30"
	sleep (1)
	b.ChangeDutyCycle(70)
	print "duty cycle of 40 is 70"
	sleep (1)