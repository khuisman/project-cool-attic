#!/usr/bin/env python

######################################################
# logs time, fahrenheit and humidity every 5 minutes
#
######################################################

import optparse, sys
import RPi.GPIO as io
import os
import time
from ../HTU21DF.py import HTU21DF
import logging
import time

try:
  import pwd
except ImportError:
  import getpass
  pwd = None

def current_user():
  if pwd:
    return pwd.getpwuid(os.geteuid()).pw_name
  else:
    return getpass.getuser()


def main():
  p = optparse.OptionParser()
  options, arguments = p.parse_args()

  if current_user() != 'root':
    print 'You must be sudo to run'
    sys.exit(0)

  if not arguments:
    logPath = '/var/log/temperature/temp-humidity.log'
  else
    logPath = arguments[0]

  setupLogging(logPath)

  while True:
    startTime = time.time()
    temp_fahrenheit = getTemperature()
    humidity = getHumidity()
    logging.info('%f\t%F', temp_fahrenheit, humidity)
    runningTime = time.time()- startTime
    time.sleep(300 - runningTime)

def setupLogging(logPath):
  logging.basicConfig(filename=logPath,level=logging.DEBUG,format='%(asctime)s\t%(message)s',datefmt='%Y-%m-%d %H:%M:%S')


def celcius_to_fahrenheit(celcius):
  return (celcius * 1.8) + 32


def median(x):
  m,r= divmod(len(x),2)
  if r:
    return sorted(x)[m]
  return sum(sorted(x)[m-1:m+1])/2

def getTemperature():
  tempList = []
  for x in range(100):
     HTU21DF.htu_reset
     tempList.append(
       celcius_to_fahrenheit(HTU21DF.read_temperature())
     )
  return median(tempList)

def getHumidity():
  tempList = []
  for x in range(100):
     HTU21DF.htu_reset
     tempList.append(HTU21DF.read_humidity())
  return median(tempList)



if __name__ == '__main__':
  main()