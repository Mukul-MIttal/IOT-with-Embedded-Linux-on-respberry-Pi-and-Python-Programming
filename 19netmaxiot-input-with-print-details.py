import time
import Netmaxiot
# Connect the Netmaxiot Button to digital port D3
button = 2
Netmaxiot.pinMode(button,"INPUT")
while True:
    try: 
    	a= Netmaxiot.digitalRead(button)
        print "kidaan ki haal chal the value is= %d" %a
        time.sleep(0.5)

    except IOError:
        print ("Error")