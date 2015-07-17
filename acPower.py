import RPi.GPIO as io

def main():
  io.setwarnings(False)
  io.setmode(io.BCM)
  io.setup(24, io.OUT)

def setState(state):
  io.output(24, state==True)

if __name__ == '__main__':
  main()
