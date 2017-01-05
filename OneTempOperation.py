import FanClass
import ReadSensor
import PWM

def AdjustPWM(FanData, CurrentSettings):
  temp = ReadSensor.ReadTemp()

  slope = (FanData.highSpeed - FanData.lowSpeed)/(FanData.highTemp - FanData.lowTemp)
  intercept = (FanData.lowSpeed*FanData.highTemp - FanData.lowTemp*FanData.highSpeed)/(FanData.highTemp - FanData.lowTemp)

  desiredPWM = slope * temp + intercept
  
