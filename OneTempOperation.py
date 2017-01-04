import FanClass
import ReadSensor

def AdjustPWM(FanData, CurrentPWM):

  temp = ReadSensor.ReadTemp()
