import json
import sys

class Config:
  def __init__(self):
    try:
      with open('config.json') as data_file:
        self._config = json.load(data_file)
    except:
      print('You must have valid config.json')
      sys.exit(0)



  def getValue(self, key=''):
    if not key:
      return self._config
    else:
      return self._config[key]

