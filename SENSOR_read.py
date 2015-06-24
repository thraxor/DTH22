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
import Adafruit_BMP.BMP085 as BMP085

#input parameters for different users
#apikey = "QRBAK77J7DZPFJ6D" 	#API key form ThingSpeak //sys.argv[1]
time_sleep = 100 		#default time between measurements
    
def getSensorData():
    DTH_RH, DTH_T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 23)
    sensor = BMP085.BMP085()
    BMP_temp = sensor.read_temperature()    # Temperature in Celcius
    BMP_pres = sensor.read_pressure()       # The local pressure
    BMP_alt = sensor.read_altitude()        # The current altitude
    BMP_sea_pres = sensor.read_sealevel_pressure() # The sea-level pressure
    
    # return dict
    return (str(DTH_RH), str(DTH_T), str(BMP_temp), str(BMP_pres), str(BMP_alt), str(BMP_sea_pres))
    
# main() function
def main():
    print 'starting measurements...'

#    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % apikey #sys.argv[1]
   
    while True:
        try:
            DTH_RH, DTH_T , BMP_temp, BMP_pres, BMP_alt, BMP_sea_pres = getSensorData()
            print DTH_RH, DTH_T
            print BMP_temp, BMP_pres, BMP_alt, BMP_sea_pres
            sleep(time_sleep)
        except:
            print 'something wrong, exiting...'
            break

# call main
if __name__ == '__main__':
    main()
