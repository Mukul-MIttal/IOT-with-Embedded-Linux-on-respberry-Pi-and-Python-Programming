import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

pins=[17,22,27,5,6,13]

for i in pins:
	GPIO.setup(i,GPIO.OUT)
while True:
	for i in pins:
		GPIO.output(i,1)
		print "LED is ON "+str(i)
		time.sleep(1)
		GPIO.output(i,0)
		print "LED is OFF "+str(i)
		time.sleep(1)