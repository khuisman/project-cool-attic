import logging


class ThLogger:

  def __init__(self, logpath):
    self.logpath = logpath
    self.setupLogging()


  def setupLogging(logPath):
    logging.basicConfig(
      level = logging.DEBUG,
      format = '%(asctime)s\t%(message)s',
      datefmt = '%Y-%m-%d %H:%M:%S',
      filename = logPath
    )


  def log(temp, humidity):
    logging.info('%f\t%F', temp, humidity)


  @classmethod
  def get(self, logpath):
    return ThLogger(logpath)

