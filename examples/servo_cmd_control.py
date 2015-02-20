from pyfirmata import ArduinoMega, time
board = ArduinoMega('/dev/ttyUSB0') # usb port
servo = board.get_pin('d:2:s') # pin PWM no 2

__copyright__ = "Copyright 2014, http://letsmakearobot.blogspot.com/"
__version__ = "0.1.0"
__license__ = "GPL"
__email__ = "sebastian.dziak@gmail.com"

def info():
    print "------------------------------------------------"
    print "Command parameters:"
    print "  0-255 - sevo position"
    print "  ...and exit from app: exit"
    print
    print "Examples:"
    print "  25"
    print "  120"
    print "  exit"
    print "------------------------------------------------"

def validate(position):
   if not position is None and (float(position)<0 or float(position)>255):
      return "Invalid parameter!"

info()
while True:
   value = raw_input('Position (0-255):')
   if value == 'exit': break  
   resp = validate(value)
   if resp is None:
      servo.write(float(value))
   else:
      print resp
 
print "goodbye"

