from pyfirmata import ArduinoMega, time
board = ArduinoMega('/dev/ttyUSB0')

while True:
   board.digital[13].write(1)
   time.sleep(1)
   board.digital[13].write(0)
   time.sleep(1)

