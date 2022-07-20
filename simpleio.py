# call the libs for hardware and others
import RPi.GPIO as GPIO
import time                                               
########  board ka mode
GPIO.setmode(GPIO.BCM) 

# kernel ki warnings band karne ke liye
GPIO.setwarnings(False) 
# pin setup output hai ke input hai
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
# pin ka status jagaooo
GPIO.output(17,True)
GPIO.output(27,True)
GPIO.output(22,True)



