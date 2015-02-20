from pyfirmata import ArduinoMega
from pyfirmata.util import Iterator
import time

board = ArduinoMega('/dev/ttyUSB0') # connect to arduino usb port

iterator = Iterator(board) # start reading analog input
iterator.start()

pinTemp = board.get_pin('a:0:i') # set valid in analog pin

while True:
    voltage = pinTemp.read() # read voltage input
    if voltage is not None: # first read after startup is somtimes None
        temp = 5.0*100*voltage # convert voltage to temperature
        print "{0} Celsius".format(temp)
        time.sleep(1) # 1 second waiting  

