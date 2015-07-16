import time 
import RPi.GPIO as io 
io.setmode(io.BCM) 
io.setup(24, io.OUT)
io.output(24, False)
