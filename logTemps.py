######################################################
# logs time, fahrenheit and humidity every 5 minutes
#
######################################################

import time
import HTU21DF
import logging
logging.basicConfig(filename='sampleDay.log',level=logging.DEBUG,format='%(asctime)s\t%(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

def celcius_to_fahrenheit(celcius):
  return (celcius * 1.8) + 32

while True:
   HTU21DF.htu_reset
   temp_fahrenheit = celcius_to_fahrenheit(HTU21DF.read_temperature())
   print("The temperature is %f F." % temp_fahrenheit)
   humidity = HTU21DF.read_humidity()
   print("The humidity is %F percent." % humidity)
   logging.info('%f\t%F', temp_fahrenheit, humidity)
   time.sleep(300)