#!/usr/bin/env python

# please install python-twitter for runing this program
# pip install python-twitter

import twitter
import time
import Netmaxiot

1_str = "8-10 Batch students doing twitter api iot readings are  =="

api = twitter.Api(
    consumer_key='M4Tasod2pbMgMKiX7YgkU0pCe',
    consumer_secret='tEuCffHndPr7xKd5srt45LsNc4hvSUfPVfBsMJ006LsH8zFdka',
    access_token_key='866192548934500352-K6SBP4UqOJS4h4JtiMKaqWgkzs0uO3u',
    access_token_secret='SC8zxjgHPD90gnN5M0PtaAaA5xONsDgn3hwCWKP2I0qQA'
    )

while True:
    # Error handling in case of problems communicating with the Netmaxiot
	try:
		lvalue = Netmaxiot.analogRead(1)
		time.sleep(0.5)
		tvalue = Netmaxiot.analogRead(0)
		light=lvalue*4.89 
		lightpercent=light/50 # light in percent
		temp= tvalue*0.489
		print "------------------------"
		print (temp)
		print "------------------------"
		print (lightpercent)
		print "-----------------"
		time.sleep(3)
		print "sending values to twitter"
		Send_str = "%s Temp= %0.2f °C, Light=%0.2f percent ," %(1_str,temp,lightpercent) #use %% for printing single %
 		time.sleep(40)
		print "----------------------------------------------------------"
		print (Send_str)
		api.PostUpdate(Send_str)
		print"-----------------------------------------"
		print"tweet send ho gaya hai check karo ji "
		time.sleep(50)
	except KeyboardInterrupt:
		print " "
		print "byeeee -----------"
		exit()

