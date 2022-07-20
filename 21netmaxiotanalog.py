import time
import Netmaxiot
a=0
while True:
	a = Netmaxiot.analogRead(0)
	print a
	time.sleep(2)
