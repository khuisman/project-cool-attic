import logging


class ThLogger:

  def __init__(self, logpath):
    self.logpath = logpath
    self.setupLogging(self.logpath)


  def setupLogging(self, logPath):
    logging.basicConfig(
      level = logging.DEBUG,
      format = '%(asctime)s\t%(message)s',
      datefmt = '%Y-%m-%d %H:%M:%S',
      filename = logPath
    )


  def log(self, temp, humidity, powerState, ambientTemp):

    message = '{0:.6f}\t{1:.6F}'.format(temp, humidity)
    if powerState:
      message += '\t{0}\t{1}'.format(
        powerState,
        ambientTemp
      )

    logging.info(message)


