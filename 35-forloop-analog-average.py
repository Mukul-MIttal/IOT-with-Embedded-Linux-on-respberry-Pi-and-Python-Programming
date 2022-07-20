import time
import Netmaxiot


def analogaverge(asensor):
        val1 = 0.0
        for i in range(20):          # take multiple samples
            val1 += (Netmaxiot.analogRead(asensor))
            time.sleep(0.5)
            print i
            print "------------------"
            print val1
            print "----------------"
        valout = val1/20
        print "the voltage in mv is =%0.2f"%valout
        return val1; 

while True:
	analogaverge(0)
	time.sleep(2)
