import FanClass
import WeatherRequest
import ReadSensor
import PWM

direction = "Clockwise"

def CalculatePWM(TwoTemp):
  temp = ReadSensor.readTemp()

  if TwoTemp.highTemp == TwoTemp.lowTemp:
    print "Cannot divide by zero!"
  else:
    slope = float(TwoTemp.highSpeed - TwoTemp.lowSpeed)/float(TwoTemp.highTemp - TwoTemp.lowTemp)
    intercept = float(float(TwoTemp.lowSpeed*TwoTemp.highTemp) - float(TwoTemp.lowTemp*TwoTemp.highSpeed))/float(TwoTemp.highTemp - TwoTemp.lowTemp)

    desiredPWM = int(round(slope * temp + intercept,0))
  
    if desiredPWM < 0:
      desiredPWM = 0

    if temp < TwoTemp.lowTemp:
      desiredPWM = 0
    elif temp >= TwoTemp.highTemp:
      desiredPWM = TwoTemp.highSpeed
  
    return desiredPWM

def CalculateDirection(TwoTemp):
  return direction

def AdjustPWM(FanData, CurrentSettings, localTemp):
  apiTemp = WeatherRequest.CurrentTemp()
  print 'Local Temp:%s API Temp:%s' % (localTemp,apiTemp)

  if FanData.highTemp == FanData.lowTemp:
    print "Cannot divide by zero!"
  else:
    slope = float(FanData.highSpeed - FanData.lowSpeed)/float(FanData.highTemp - FanData.lowTemp)
    intercept = float(float(FanData.lowSpeed*FanData.highTemp) - float(FanData.lowTemp*FanData.highSpeed))/float(FanData.highTemp - FanData.lowTemp)

    desiredPWM = int(round(slope * localTemp + intercept,0))

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

    direction = FanData.direction
    CurrentSettings = PWM.adjustpwm(FanData, CurrentSettings)

    return CurrentSettings
