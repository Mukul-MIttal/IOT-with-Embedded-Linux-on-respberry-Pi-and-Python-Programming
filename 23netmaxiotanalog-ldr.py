import time
import Netmaxiot

while True:
	valueread1 = Netmaxiot.analogRead(0)
	valueread2 = Netmaxiot.analogRead(1)
	valueread3 = Netmaxiot.analogRead(2)
	valueread4 = Netmaxiot.analogRead(3)
	print "the value on adc 1 is ==%d"%valueread1
	print "the voltage in mv is =%0.2f"%voltage1
	voltage1 = valueread1 * 4.89#5000/1023

	temp=voltage1/10	# as 10mv=1c
	

	print " the temp is ==%0.2f *C " %temp
	print "-------------------------------------"
	print "the value on adc  is ==%d"%valueread2
	print "------------------------------------------"
	voltage2 = valueread2 * 4.89
	lightintensity = (voltage2/5000)#5v is max 
	print "the value on Light   is ==%0.2f "%(lightintensity*100)
	time.sleep(2)
	print "-----------------"
