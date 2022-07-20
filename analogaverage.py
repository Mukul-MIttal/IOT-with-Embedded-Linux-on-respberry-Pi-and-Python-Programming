from time import sleep
import Netmaxiot
sensor_pin=A0
Netmaxiot.pinMode(sensor_pin,"INPUT")
voltage=0
try:
	while True:
		for i in range(0,25):
			adcvalue=Netmaxiot.analogRead(sensor_pin)
			voltage=adcvalue*0.0048
			voltage+=voltage
			sleep(0.5)
		print"Average Voltage is = "+voltage
except KeyboardInterrupt:
	print "_____KeyboardInterrupt_____ "