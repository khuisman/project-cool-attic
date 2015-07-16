import optparse, sys, os

## setup import from parent directory
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )


class CLI:

  def __init__(self):
    p = optparse.OptionParser()
    options, arguments = p.parse_args()

    self.options = options
    self.arguments = arguments


  def isRootOrDie(self):
    ## pwd or getpass used to determine if user is root
    try:
      import pwd
    except ImportError:
      import getpass
      pwd = None

    if pwd:
      user = pwd.getpwuid(os.geteuid()).pw_name
    else:
      user = getpass.getuser()

    if user != 'root':
      print 'You must be root to run this command'
      sys.exit(0)

  def getArgs(self):
    return self.arguments

  def getOptions(self):
    return self.options


