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
import ReadSensor

# Sleeps the process on Startup to let the WebServer start.
time.sleep(4)

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Hall Effect GPIO Pin 11
GPIO.setup(6, GPIO.OUT) # Changer Power LED GPIO Pin 6
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change OP Mode GPIO Pin 17
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change Direction GPIO Pin 21
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Change Power GPIO Pin 5

GPIO.output(15, GPIO.HIGH) # Set Direction to Default Forwards
AccessWebServer.PostPower("false") # Set WebServer Power Status to Default Off

GPIO.output(6, GPIO.LOW) # Set Power LED to Default Off

AccessWebServer.PostMessage(Internet.getNow()+ '\n' + Internet.getIP())
#time.sleep(2)

currentSettings = FanClass.CurrentFanData("Clockwise",-1)
stringTemp = "0"

def power_callback(channel):
  fanStatus = AccessWebServer.GetOp()

  if fanStatus.power:
    AccessWebServer.PostPower("false")
    GPIO.output(6, GPIO.LOW)
    AccessWebServer.PostMessage("Power Off" + '\n' + "Temp: " + stringTemp)
  else:
    AccessWebServer.PostPower("true")
    GPIO.output(6, GPIO.HIGH)
    AccessWebServer.PostMessage("Power On" + '\n' + "Temp: " + stringTemp)
    
def opMode_callback(channel):
  fanStatus = AccessWebServer.GetOp()
  if fanStatus.mode == "Manual":
    AccessWebServer.PostOp("OneTemp",fanStatus.rpm)
    AccessWebServer.PostMessage(" Mode       Temp\nTemperature " + stringTemp)
  elif fanStatus.mode == "OneTemp":
    AccessWebServer.PostOp("Schedule",fanStatus.rpm)
    AccessWebServer.PostMessage(" Mode       Temp\nSchedule    " + stringTemp)
  elif fanStatus.mode == "Schedule":
    AccessWebServer.PostOp("TwoTemp",fanStatus.rpm) 
    AccessWebServer.PostMessage(" Mode       Temp\nWindow      " + stringTemp)
  elif fanStatus.mode == "TwoTemp":
    AccessWebServer.PostOp("Manual",fanStatus.rpm)
    AccessWebServer.PostMessage(" Mode       Temp\nManual      " + stringTemp)
  else:
    AccessWebServer.PostOp("Manual",fanStatus.rpm)
    AccessWebServer.PostMessage(" Mode       Temp\nManual      " + stringTemp)

def direction_callback(channel):
  currentManual = AccessWebServer.GetManual()
  fanStatus = AccessWebServer.GetOp()
  
  if currentManual.direction.lower() == "clockwise":
    manualData = FanClass.ManualData("Counterclockwise", currentManual.pwm)
    AccessWebServer.PostManual(manualData)
    AccessWebServer.PostMessage("Direction Temp\nBackwards " + stringTemp)
  elif currentManual.direction.lower() == "counterclockwise":
    manualData = FanClass.ManualData("Clockwise", currentManual.pwm)
    AccessWebServer.PostManual(manualData)
    AccessWebServer.PostMessage("Direction Temp\nForwards  " + stringTemp)
    
  AccessWebServer.PostOp("Manual",fanStatus.rpm)

previousTime = time.time()
postTime = previousTime

def hallEffect_callback(channel):
  global previousTime
  global postTime
  global currentSettings
  
  if time.time() - postTime > 5:
    postTime = time.time()
    rpm = 60 / (time.time() - previousTime)
    fanStatus = AccessWebServer.GetOp()
    AccessWebServer.PostOp(fanStatus.mode,rpm)
        
  previousTime = time.time()
    
def exit_handler():
  print "Turning off the PWM for safety!"
  global currentSettings

  while currentSettings.pwm > 0:
    currentSettings.pwm = currentSettings.pwm - 4
    print "Reducing output to: " + str(currentSettings.pwm)
    PWM.setpwm(currentSettings.pwm)
    time.sleep(0.25)

  currentSettings.pwm = -1
  PWM.setpwm(-1)
  GPIO.cleanup()
  
atexit.register(exit_handler)

def handler(signum, frame):
  print 'Ctrl+Z pressed, but ignored'
  
signal.signal(signal.SIGTSTP, handler)

GPIO.add_event_detect(17, GPIO.RISING, callback=opMode_callback, bouncetime=1000)
GPIO.add_event_detect(5, GPIO.RISING, callback=power_callback, bouncetime=1000)
GPIO.add_event_detect(21, GPIO.RISING, callback=direction_callback, bouncetime=1000)
GPIO.add_event_detect(11, GPIO.FALLING, callback=hallEffect_callback, bouncetime=50)

PWM.setuppwm()

while True:
  fanStatus = AccessWebServer.GetOp()
  temp = ReadSensor.readTemp()
  stringTemp = str(int(temp)) + " F"

  if stringTemp == "-3000":
    stringTemp = "N/A"
  
  if fanStatus.rpm != 0 and time.time() - previousTime > 3:
    AccessWebServer.PostOp(fanStatus.mode, 0)
  
  if fanStatus.power:
    GPIO.output(6, GPIO.HIGH)
    currentSettings.mode = fanStatus.mode

    if currentSettings.mode == "Manual":
      manualData = AccessWebServer.GetManual()
      currentSettings = ManualOperation.AdjustPWM(manualData, currentSettings)
  
    elif currentSettings.mode == "Schedule":
      scheduleData = AccessWebServer.GetCurrentSchedule()
      currentSettings = ScheduleOperation.AdjustPWM(scheduleData, currentSettings)

    elif currentSettings.mode == "OneTemp":
      oneTempData = AccessWebServer.GetOneTemp()
      currentSettings = OneTempOperation.AdjustPWM(oneTempData, currentSettings, temp)

    elif currentSettings.mode == "TwoTemp":
      twoTempData = AccessWebServer.GetTwoTemp()
      currentSettings = TwoTempOperation.AdjustPWM(twoTempData, currentSettings, temp)
  
    else:
      #print "Currently in: " + currentSettings.mode + " which is not an operation mode."
      AccessWebServer.PostOp("Manual",fanStatus.rpm)

      while currentSettings.pwm > 0:
        currentSettings.pwm = currentSettings.pwm - 4
        print "Reducing output to: " + str(currentSettings.pwm)
        PWM.setpwm(currentSettings.pwm)
        time.sleep(0.25)
        
      PWM.setpwm(-1)

  else:
    GPIO.output(6, GPIO.LOW)

    while currentSettings.pwm > 0:
      currentSettings.pwm = currentSettings.pwm - 4
      print "Reducing output to: " + str(currentSettings.pwm)
      PWM.setpwm(currentSettings.pwm)
      time.sleep(0.25)

    currentSettings.pwm = -1
    PWM.setpwm(-1)
  
  time.sleep(.5)
