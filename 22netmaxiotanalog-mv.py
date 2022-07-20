import time
import Netmaxiot

while True:
	valueread = Netmaxiot.analogRead(0)
	print "the value on adc is ==%d"%valueread
	voltage = valueread * 4.89
	print "the voltage in mv is =%0.2f"%voltage
	temp=voltage/10
	print " the temp is ==%0.2f *C " %temp
	time.sleep(2)
