"""
dht11_thingspeak.py

Temperature/Humidity monitor using Raspberry Pi and DHT11. 
Data is displayed at thingspeak.com

Author: Mahesh Venkitachalam
Website: electronut.in

"""

import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2

#input parameters for different users
apikey = "QRBAK77J7DZPFJ6D" 	#API key form ThingSpeak //sys.argv[1]
time_sleep = 100 		#default time between measurements
    
def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23)
    # return dict
    return (str(RH), str(T))
    
# main() function
def main():
    # use sys.argv if needed
    # if len(sys.argv) < 2:
    #    print('Usage: python tstest.py PRIVATE_KEY')
    #    exit(0)
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % apikey #sys.argv[1]
   
    while True:
        try:
            RH, T = getSensorData()
            f = urllib2.urlopen(baseURL + 
                                "&field1=%s&field2=%s" % (T, RH))
            print f.read()
            f.close()
            sleep(time_sleep)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
