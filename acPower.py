import RPi.GPIO as io

def setup():
  io.setwarnings(False)
  io.setmode(io.BCM)
  io.setup(24, io.OUT)

def setState(state):
  io.output(24, state==True)

