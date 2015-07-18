## http://api.openweathermap.org/data/2.5/weather?zip=98155,us&units=imperial&appid=
import config
import requests
import logging

logging.getLogger("requests").setLevel(logging.WARNING)


def getLocalTemperature():

  conf = config.Config()
  path = '/data/2.5/weather?zip={0},us&units=imperial&appid={1}'.format(
    conf.getValue('openweathermap_zipcode'),
    conf.getValue('openweathermap_appid')
  )

  data = 0

  try:
    r = requests.get('http://api.openweathermap.org' + path)
    contents = r.json()
    data = contents['main']['temp']
  except:
    pass


  return data
