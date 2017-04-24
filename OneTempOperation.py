import FanClass
import ReadSensor
import PWM

def CalculatePWM(OneTemp):
  temp = ReadSensor.readTemp()


  if OneTemp.highTemp == OneTemp.lowTemp:
    print "Cannot divide by zero!"
  else:
    slope = float(OneTemp.highSpeed - OneTemp.lowSpeed)/float(OneTemp.highTemp - OneTemp.lowTemp)
    intercept = float(float(OneTemp.lowSpeed*OneTemp.highTemp) - float(OneTemp.lowTemp*OneTemp.highSpeed))/float(OneTemp.highTemp - OneTemp.lowTemp)

    desiredPWM = int(round(slope * temp + intercept,0))

    if desiredPWM < 0:
      desiredPWM = 0

    if temp < OneTemp.lowTemp:
      desiredPWM = 0
    elif temp >= OneTemp.highTemp:
      desiredPWM = OneTemp.highSpeed

    return desiredPWM

  
def AdjustPWM(FanData, CurrentSettings, temp):
  #temp = ReadSensor.readPotent() # Using a potentiometer for testing

  print temp

  if FanData.highTemp == FanData.lowTemp:
    print "Cannot divide by zero!"
  else:
    slope = float(FanData.highSpeed - FanData.lowSpeed)/float(FanData.highTemp - FanData.lowTemp)
    intercept = float(float(FanData.lowSpeed*FanData.highTemp) - float(FanData.lowTemp*FanData.highSpeed))/float(FanData.highTemp - FanData.lowTemp)
    
    desiredPWM = int(round(slope * temp + intercept,0))
  
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
