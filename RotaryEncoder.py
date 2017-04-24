import time
import FanClass
import AccessWebServer
import gaugette.rotary_encoder as rotary
import LCDcontrol as lcd
import OneTempOperation
import TwoTempOperation

A_PIN = 28
B_PIN = 26

encoder = rotary.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()

rightChar = ">"
leftChar = "<"

manualData = AccessWebServer.GetManual()

pwm = manualData.pwm
direction = manualData.direction
speed = ""
maxSpeed = 52

while True:
  delta = encoder.get_delta() / 4.0
  
  if delta != 0:
    operationMode = AccessWebServer.GetOp()
    if operationMode.mode == "Manual":
      manual = AccessWebServer.GetManual()
      direction = manual.direction
      pwm = manual.pwm
    elif operationMode.mode == "OneTemp":
      oneTemp = AccessWebServer.GetOneTemp()
      direction = oneTemp.direction
      pwm = OneTempOperation.CalculatePWM(oneTemp)
      print pwm
    elif operationMode.mode == "TwoTemp":
      twoTemp = AccessWebServer.GetTwoTemp()
      direction = TwoTempOperation.CalculateDirection(twoTemp)
      pwm = TwoTempOperation.CalculatePWM(twoTemp)
    elif operationMode.mode == "Schedule":
      schedule = AccessWebServer.GetCurrentSchedule()
      direction = schedule.direction
      pwm = schedule.pwm
      
    if (pwm + delta) > maxSpeed:
      pwm = maxSpeed
    elif (pwm + delta) < 0:
      pwm = 0
    else:
      pwm = pwm + delta

    manualData.pwm = pwm
    manualData.direction = direction

    if pwm == maxSpeed:
      speed = "Maximum Speed"
    elif pwm == 0:
      speed = "Minimum Speed"
    else:
      pwmLCD = pwm / 2
      secondLine = pwmLCD - 16
      if direction.lower() == "clockwise":
        topLine = rightChar * int(pwmLCD)
        bottomLine = '\n' + rightChar * int(secondLine)

        if pwm % 2 == 1:
          if pwmLCD <= 16:
            topLine = topLine + "_"
          else:
            bottomLine = bottomLine + "_"

        speed = topLine + bottomLine
      elif direction.lower() == "counterclockwise":
        topLine = leftChar * int(pwmLCD)
        bottomLine = '\n' + leftChar * int(secondLine)
        
        if pwm % 2 == 1:
          if pwmLCD <= 16:
            topLine = topLine + "_"
          else:
            bottomLine = bottomLine + "_"
            
        speed = topLine + bottomLine

    AccessWebServer.PostManual(manualData)
    AccessWebServer.PostOp("Manual", operationMode.rpm)
    AccessWebServer.PostMessage(speed)
    
  time.sleep(1)

