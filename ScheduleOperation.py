import FanClass
import PWM

def AdjustPWM(FanData, CurrentSettings):

  CurrentSettings = PWM.adjustpwm(FanData, CurrentSettings)

  return CurrentSettings
