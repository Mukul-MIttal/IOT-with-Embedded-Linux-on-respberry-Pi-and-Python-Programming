import json
import sys
import time
import datetime
import Adafruit_DHT
import gspread
import Netmaxiot
from oauth2client.service_account import ServiceAccountCredentials
DHT_TYPE = Adafruit_DHT.DHT11
DHT_PIN  = 4

GDOCS_OAUTH_JSON       = '27-10-12.json'
GDOCS_SPREADSHEET_NAME = 'iot data with analog'
FREQUENCY_SECONDS      = 10

############################################################

def login_open_sheet(oauth_key_file, spreadsheet):
    """Connect to Google Docs spreadsheet and return the first worksheet."""
    try:
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
        gc = gspread.authorize(credentials)
        worksheet = gc.open(spreadsheet).sheet1
        return worksheet
    except Exception as ex:
        print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
        print('Google sheet login failed with error:', ex)
        sys.exit(1)


print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
print('Press Ctrl-C to quit.')

worksheet = None

while True:
        # Login if necessary.
    valueread1 = Netmaxiot.analogRead(0)
    valueread2 = Netmaxiot.analogRead(1)
    voltage1 = valueread1 * 4.89#5000/1023
    atemp=voltage1/10    # as 10mv=1c
    voltage2 = valueread2 * 4.89
    light = (voltage2/50)

    if worksheet is None:
        worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)
        print "login to google sheet with login details"
    
    print "---------------------------------------------"
    humidity, temp = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    nowx=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
    print(temp)
    print(humidity)
    print(nowx)
    if humidity is None or temp is None:
        time.sleep(2)
        continue
    
    try:
      worksheet.append_row((nowx,temp,humidity,atemp,light))
      print "***************************************************"
      
    except:
      print('Append error, logging in again')
      worksheet = None
      time.sleep(FREQUENCY_SECONDS)
      continue

    print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
    time.sleep(FREQUENCY_SECONDS)
    print (FREQUENCY_SECONDS) 
    print "***************************************************"
