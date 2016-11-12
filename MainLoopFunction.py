import atexit
import signal
import PWM
#import ScheduleOperation
#import ManualOperation
#import OneSourceTemperatureOperation
#import TwoSourceTemperatureOperation
import Settings
import AccessWebServer
import time

def exit_handler():
    print "Turning off the PWM for safety!"
    PWM.setpwm(-1)
  
atexit.register(exit_handler)

def handler(signum, frame):
    print 'Ctrl+Z pressed, but ignored'
  
signal.signal(signal.SIGTSTP, handler)

PWM.setuppwm()

currentPWM = -1

# Get last operation mode used
    # Access DB or web server to find value
    # If none exists use default mode (manual?)
  
#Settings.ReadSettings(Settings.OperationMode.Manual)

#fanData = AccessWebServer.GetCurrentFanData()

#fanData.roomTemp = 75
#fanData.fanSpeed = 3700

#AccessWebServer.PostUpdateFanData(fanData)

while True:
  fanData = AccessWebServer.GetCurrentFanData()
  
  print "Setting PWM to: " + str(fanData.fanSpeed)
  PWM.setpwm(fanData.fanSpeed)

  time.sleep(1)
     
#    currentPWM = currentPWM + 1;
  
#    time.sleep(.01)
  
    # Call specific function for operation mode
        # CurrentPWM = Temp Mode 1 (CurrentPWM) Returns new PWM value
        # CurrentPWM = Temp Mode 2 (CurrentPWM) Returns new PWM value
        # CurrentPWM = Schedule Mode (CurrentPWM) Returns new PWM value
        # CurrentPWM = Manual Mode (CurrentPWM) Returns new PWM value
  
    # Access current operation mode from DB or web server
