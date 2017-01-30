import FanClass
import WeatherRequest
import ReadSensor
import PWM

def AdjustPWM(FanData, CurrentSettings):
  #temp = ReadSensor.readTemp()
   
  localTemp = ReadSensor.readPotent()
  apiTemp = WeatherRequest.CurrentTemp()

  print 'Local Temp:%s API Temp:%s' % (localTemp,apiTemp)

  slope = float(FanData.highSpeed - FanData.lowSpeed)/float(FanData.highTemp - FanData.lowTemp)
  intercept = float(float(FanData.lowSpeed*FanData.highTemp) - float(FanData.lowTemp*FanData.highSpeed))/float(FanData.highTemp - FanData.lowTemp)

  desiredPWM = round(slope * localTemp + intercept,0)

  if desiredPWM < 0:
    desiredPWM = 0

  if localTemp < FanData.lowTemp:
    desiredPWM = 0
  elif localTemp >= FanData.highTemp:
    desiredPWM = FanData.highSpeed

  FanData.pwm = desiredPWM

  # Subtracts the two temperates
  differential = localTemp - apiTemp

  # If the difference between the two temperatures is greater than 2 degrees in either direction
  # set the direction and the differential
  if differential > 2.0:
    FanData.direction = "Clockwise"
    CurrentSettings.differential = "localTemp"
  elif differential < -2.0:
    FanData.direction = "Counterclockwise"
    CurrentSettings.differential = "apiTemp"
  else:
    if CurrentSettings.differential == "localTemp":
      FanData.direction = "Clockwise"
    elif CurrentSettings.differential == "apiTemp":
      FanData.direction = "Counterclockwise"
    else:
      FanData.direction = "Clockwise"
      CurrentSettings.differential = "localTemp"

  CurrentSettings = PWM.adjustpwm(FanData, CurrentSettings)

  return CurrentSettings
