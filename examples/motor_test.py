from pyfirmata import ArduinoMega
board = ArduinoMega('/dev/ttyUSB0')

__copyright__ = "Copyright 2014, http://letsmakearobot.blogspot.com/"
__version__ = "0.2.0"
__license__ = "GPL"
__email___ = "sebastian.dziak@gmail.com"

pin_motor_A_L = board.get_pin('d:4:p')
pin_motor_A_R = board.get_pin('d:5:p')
pin_motor_B_R = board.get_pin('d:6:p')
pin_motor_B_L = board.get_pin('d:7:p')

cmd_motor = ('A','B')
cmd_direction = ('L','R','S')
invalid_number_parameters = "Invalid number of parameters!"
invalid_parameter = "Invalid parameter: "

def set_motor(motor, cmd, speed):
if args[0]=='A':
    if cmd=='S':
    pin_motor_A_L.write(0)  
    pin_motor_A_R.write(0)  
    elif cmd=='L':
    pin_motor_A_R.write(0)             
    pin_motor_A_L.write(speed)  
    elif cmd=='R':
    pin_motor_A_L.write(0)  
    pin_motor_A_R.write(speed)  

if args[0]=='B':
    if cmd=='S':
    pin_motor_B_L.write(0)  
    pin_motor_B_R.write(0)  
    elif cmd=='L':
    pin_motor_B_R.write(0)             
    pin_motor_B_L.write(speed)  
    elif cmd=='R':
    pin_motor_B_L.write(0)  
    pin_motor_B_R.write(speed)  


def info():
print "------------------------------------------------"
print "Command parameters:"
print "  A,B - motor id"
print "  L,R,S - L - left rotation, R - right rotation, S - motor stop"
print "  0.0-1.0 - velocity (should be given only with the option of L or R)"
print "  ...and exit from app: exit"
print   
print "Examples:"
print "  A R 0.4"
print "  A S"
print "------------------------------------------------"

def validate(engine, cmd, speed):
if engine not in cmd_motor:
    return invalid_parameter+engine
elif cmd not in cmd_direction:
    return invalid_parameter+cmd
elif cmd=='S' and not speed is None:
    return invalid_number_parameters
elif (cmd=='L' or cmd=='R') and speed is None:
    return invalid_number_parameters
elif not speed is None and (float(speed)<0.0 or float(speed)>1.0):
     return invalid_parameter+speed

info()
while True:
cmdLine = raw_input('CMD (A/B L/R/S 0.0-1.0):')
if cmdLine == 'exit': break    

args = cmdLine.split() 

if len(args)>0:    
    engine = args[0]
else:
    engine = None

if len(args)>1:    
    cmd = args[1]
else:
    cmd = None

if len(args)>2:    
speed = float(args[2])
else:
speed = None       

resp = validate(engine, cmd, speed)

if resp is None:
set_motor(engine, cmd, speed)
else:
print resp

print "goodbye"

