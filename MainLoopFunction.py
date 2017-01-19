import atexit
import signal
import time
import RPi.GPIO as GPIO
import PWM
import FanClass
import LCDcontrol as lcd
import AccessWebServer
import ManualOperation
#import ScheduleOperation
import OneTempOperation
#import TwoTempOperation

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # POWER PUSH BUTTON GPIO PIN 5
GPIO.setup(6, GPIO.OUT)
GPIO.setup(6, GPIO.LOW) # LED INDICATOR GPIO PIN 6

lcd.setBacklight(0)

currentSettings = FanClass.CurrentFanData("Clockwise",-1,True)

def power_callback(channel):
  global currentSettings
  if currentSettings.power:
    currentSettings.power = False
    GPIO.output(6, GPIO.LOW)
    print "Power Off"
  else:
    currentSettings.power = True
    GPIO.output(6, GPIO.HIGH)
    print "Power On"

def exit_handler():
  print "Turning off the PWM for safety!"
  PWM.setpwm(-1)
  
atexit.register(exit_handler)

def handler(signum, frame):
  print 'Ctrl+Z pressed, but ignored'
  
signal.signal(signal.SIGTSTP, handler)

PWM.setuppwm()

while True:
  opMode = AccessWebServer.GetOp()
  
  if opMode == "Manual":
    manualData = AccessWebServer.GetManual()
    currentSettings = ManualOperation.AdjustPWM(manualData, currentSettings)
  
  elif opMode == "Schedule":
    print "Schedule is not Implemented yet"

  elif opMode == "OneTemp":
    oneTempData = AccessWebServer.GetOneTemp()
    currentSettings = OneTempOperation.AdjustPWM(oneTempData, currentSettings)

  elif opMode == "TwoTemp":
    twoTempData = AccessWebServer.GetTwoTemp()
    print "TwoTemp is not Implemented yet"
  
  else:
    print "Not in Manual or OneTemp"
    PWM.setpwm(-1)
  
  if currentSettings.direction.lower() == "clockwise":
    lcd.writeClear('PWM ' + str(currentSettings.pwm) + ' Clockwise')
  elif currentSettings.direction.lower() == "counterclockwise":
    lcd.writeClear('PWM ' + str(currentSettings.pwm) + '\nCounterclockwise')
  time.sleep(1)
