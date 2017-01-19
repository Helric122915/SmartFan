import FanClass
import ReadSensor
import PWM

def AdjustPWM(FanData, CurrentSettings):
  #temp = ReadSensor.readTemp()
  temp = ReadSensor.readPotent() # Using a potentiometer for testing

  slope = float(FanData.highSpeed - FanData.lowSpeed)/float(FanData.highTemp - FanData.lowTemp)
  intercept = float(float(FanData.lowSpeed*FanData.highTemp) - float(FanData.lowTemp*FanData.highSpeed))/float(FanData.highTemp - FanData.lowTemp)

  desiredPWM = round(slope * temp + intercept,0)
  
  if desiredPWM < 0:
    desiredPWM = 0

  if temp < FanData.lowTemp:
    desiredPWM = 0
  elif temp >= FanData.highTemp:
    desiredPWM = FanData.highSpeed

  print "PWM: " + str(desiredPWM)
  print "temp: " + str(temp)

  CurrentSettings = PWM.adjustpwm(FanData, CurrentSettings):
  #if FanData.direction.lower() == "clockwise" or FanData.direction.lower() == "counterclockwise":
  #  if CurrentSettings.direction == FanData.direction:
  #    if CurrentSettings.pwm < desiredPWM:
  #      CurrentSettings.pwm = CurrentSettings.pwm + 1
  #      PWM.setpwm(CurrentSettings.pwm)
  #      print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction

  #    elif CurrentSettings.pwm > desiredPWM:
  #      CurrentSettings.pwm = CurrentSettings.pwm - 1
  #      PWM.setpwm(CurrentSettings.pwm)
  #      print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction   

  #   else:
  #     if CurrentSettings.pwm == 0 or CurrentSettings.pwm == -1:
  #        CurrentSettings.direction = FanData.direction
  #        print "Changing Direction of Fan"
  #     else:
  #       CurrentSettings.pwm = CurrentSettings.pwm - 1
  #       PWM.setpwm(CurrentSettings.pwm)
  #       print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction

  return CurrentSettings
