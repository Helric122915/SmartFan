import atexit
import signal
import PWM
import FanClass
#import ScheduleOperation
import ManualOperation
#import OneSourceTemperatureOperation
#import TwoSourceTemperatureOperation
import Settings
import AccessWebServer
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_UP) # POWER PUSH BUTTON GPIO PIN 4
GPIO.setup(3, GPIO.OUT)
GPIO.setup(3, GPIO.LOW) # LED INDICATOR GPIO PIN 3

currentSettings = FanClass.CurrentFanData("Clockwise",-1,True)

def power_callback(channel):
  global currentSettings
  if currentSettings.power:
    currentSettings.power = False
    GPIO.output(3, GPIO.LOW)
    print "Power Off"
  else:
    currentSettings.power = True
    GPIO.output(3, GPIO.HIGH)
    print "Power On"

def exit_handler():
  print "Turning off the PWM for safety!"
  PWM.setpwm(-1)
  
atexit.register(exit_handler)

def handler(signum, frame):
  print 'Ctrl+Z pressed, but ignored'
  
signal.signal(signal.SIGTSTP, handler)

PWM.setuppwm()

manualData = AccessWebServer.GetManual()

while True:
  opMode = AccessWebServer.GetOp()
  
  if opMode == "Manual":
    manualData = AccessWebServer.GetManual()
    currentSettings = ManualOperation.AdjustPWM(manualData, currentSettings)

  else:
    print "Not in Manual"
    PWM.setpwm(-1)

  time.sleep(1)
     
#    currentPWM = currentPWM + 1;
  
#    time.sleep(.01)
  
    # Call specific function for operation mode
        # CurrentPWM = Temp Mode 1 (CurrentPWM) Returns new PWM value
        # CurrentPWM = Temp Mode 2 (CurrentPWM) Returns new PWM value
        # CurrentPWM = Schedule Mode (CurrentPWM) Returns new PWM value
        # CurrentPWM = Manual Mode (CurrentPWM) Returns new PWM value
  
    # Access current operation mode from DB or web server
