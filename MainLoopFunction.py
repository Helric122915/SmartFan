import atexit
import signal
import time
import RPi.GPIO as GPIO
import PWM
import FanClass
import LCDcontrol as lcd
import AccessWebServer
import ManualOperation
import ScheduleOperation
import OneTempOperation
import TwoTempOperation
import Internet

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP) # POWER PUSH BUTTON GPIO PIN 16
GPIO.setup(6, GPIO.OUT)
GPIO.setup(6, GPIO.LOW) # LED INDICATOR GPIO PIN 6
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change Mode PIN 12
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change Direction PIN 21

GPIO.output(6, GPIO.HIGH)

lcd.StartUp()

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

def opMode_callback(channel):
  global currentSettings
  if currentSettings.mode == "Manual":
    AccessWebServer.PostOp("OneTemp")
    lcd.writeClear("OneTemp")
  elif currentSettings.mode == "OneTemp":
    AccessWebServer.PostOp("Schedule")
    lcd.writeClear("Schedule")
  elif currentSettings.mode == "Schedule":
    AccessWebServer.PostOp("TwoTemp") 
    lcd.writeClear("TwoTemp")
  elif currentSettings.mode == "TwoTemp":
    AccessWebServer.PostOp("Manual")
    lcd.writeClear("Manual")
  else:
    AccessWebServer.PostOp("N/A")
    lcd.writeClear("Op Mode Undefined")

def direction_callback(channel):
  global currentSettings
  
  currentManual = AccessWebServer.GetManual()

  if currentManual.direction.lower() == "clockwise":
    manualData = FanClass.ManualData("Counterclockwise", currentManual.pwm)
    AccessWebServer.PostManual(manualData)
  elif currentManual.direction.lower() == "counterclockwise":
    manualData = FanClass.ManualData("Clockwise", currentManual.pwm)
    AccessWebServer.PostManual(manualData)

  AccessWebServer.PostOp("Manual")
  

def exit_handler():
  print "Turning off the PWM for safety!"
  PWM.setpwm(-1)
  lcd.clear()
  lcd.setBacklight(1)
  GPIO.cleanup()
  
atexit.register(exit_handler)

def handler(signum, frame):
  print 'Ctrl+Z pressed, but ignored'
  
signal.signal(signal.SIGTSTP, handler)

GPIO.add_event_detect(12, GPIO.RISING, callback=opMode_callback, bouncetime=1000)
GPIO.add_event_detect(16, GPIO.RISING, callback=power_callback, bouncetime=1000)
GPIO.add_event_detect(21, GPIO.RISING, callback=direction_callback, bouncetime=1000)

PWM.setuppwm()

while True:
  currentSettings.mode = AccessWebServer.GetOp()  

  if currentSettings.power:
    if currentSettings.mode == "Manual":
      manualData = AccessWebServer.GetManual()
      currentSettings = ManualOperation.AdjustPWM(manualData, currentSettings)
  
    elif currentSettings.mode == "Schedule":
      scheduleData = AccessWebServer.GetCurrentSchedule()
      currentSettings = ScheduleOperation.AdjustPWM(scheduleData, currentSettings)

    elif currentSettings.mode == "OneTemp":
      oneTempData = AccessWebServer.GetOneTemp()
      currentSettings = OneTempOperation.AdjustPWM(oneTempData, currentSettings)

    elif currentSettings.mode == "TwoTemp":
      twoTempData = AccessWebServer.GetTwoTemp()
      currentSettings = TwoTempOperation.AdjustPWM(twoTempData, currentSettings)
  
    else:
      print "Not in an operation mode."
      PWM.setpwm(-1)
 
    #if currentSettings.direction.lower() == "clockwise":
    #  lcd.writeClear('PWM ' + str(currentSettings.pwm) + ' Clockwise')
    #elif currentSettings.direction.lower() == "counterclockwise":
    #  lcd.writeClear('PWM ' + str(currentSettings.pwm) + '\nCounterclockwise')

  else:
    settings = FanClass.CurrentFanData("Clockwise",-1,False)
    zeroOut = FanClass.ManualData("Clockwise",-1)
    ManualOperation.AdjustPWM(settings,zeroOut)
  
  if currentSettings.direction.lower() == "clockwise":
    lcd.writeClear('PWM ' + str(currentSettings.pwm) + ' Clockwise')
  elif currentSettings.direction.lower() == "counterclockwise":
    lcd.writeClear('PWM ' + str(currentSettings.pwm) + '\nCounterclockwise')

  time.sleep(.5)
