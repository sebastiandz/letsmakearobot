from pyfirmata import ArduinoMega, time
board = ArduinoMega('/dev/ttyUSB0')
firstPin = 22 # number first pin, app use 8 pins

__copyright__ = "Copyright 2014, http://letsmakearobot.blogspot.com/"
__version__ = "0.1.0"
__license__ = "GPL"
__email__ = "sebastian.dziak@gmail.com"

def info():
    print "------------------------------------------------"
    print "Command parameters:"
    print "  1-8 - relay no"
    print "  0-1 - relay status (0 - off, 1 - on)"
    print "  ...and exit from app: exit"
    print 
    print "Examples:"
    print "  2 1 #set on relay no 2"
    print "  2 0 #set off relay no 2"
    print "  5 1 #set off realy no 5 "
    print "  exit"
    print "------------------------------------------------"

def validate(position):
   if not position is None and (float(position)<0 or float(position)>255):
      return "Invalid parameter!"

info()

pins = []
for n in range (0, 8):
   pinNo = firstPin + n
   pins.append( board.get_pin('d:'+str(pinNo)+':o') )

while True:
   cmdLine = raw_input('Relay_no(1-8) set_status(0-1):')
   if cmdLine == 'exit': break 
   args = cmdLine.split()
   pins[int(args[0])-1].write(int(args[1]))

print "goodbye"

