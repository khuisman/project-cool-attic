######################################################
# logs time, fahrenheit and humidity every 5 minutes
#
######################################################

import time
import HTU21DF
import logging
logging.basicConfig(filename='/var/log/temperature/temp-humidity.log',level=logging.DEBUG,format='%(asctime)s\t%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

def celcius_to_fahrenheit(celcius):
  return (celcius * 1.8) + 32

while True:
   HTU21DF.htu_reset
   temp_fahrenheit = celcius_to_fahrenheit(HTU21DF.read_temperature())
   humidity = HTU21DF.read_humidity()
   logging.info('%f\t%F', temp_fahrenheit, humidity)
   time.sleep(300)
