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

  FanData.pwm = desiredPWM

  CurrentSettings = PWM.adjustpwm(FanData, CurrentSettings)

  return CurrentSettings
