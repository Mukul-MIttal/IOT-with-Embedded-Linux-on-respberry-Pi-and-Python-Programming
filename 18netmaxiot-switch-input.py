#!/usr/bin/env python

import time
import Netmaxiot
# Connect the Netmaxiot Button to digital port D3
button = 1
Netmaxiot.pinMode(button,"INPUT")
while True:
    try: 
    	print(Netmaxiot.digitalRead(button))
        time.sleep(0.5)

    except IOError:
        print ("Error")