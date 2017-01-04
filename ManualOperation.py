import FanClass
import PWM

def AdjustPWM(FanData, CurrentSettings):
  if FanData.direction == "Clockwise" or FanData.direction == "Counterclockwise":
    if CurrentSettings.direction == FanData.direction:
      if CurrentSettings.pwm < FanData.pwm:
        CurrentSettings.pwm = CurrentSettings.pwm + 1
        PWM.setpwm(CurrentSettings.pwm)
        print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction

      elif CurrentSettings.pwm > FanData.pwm:
        CurrentSettings.pwm = CurrentSettings.pwm - 1
        PWM.setpwm(CurrentSettings.pwm)
        print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction   

    else:
       if CurrentSettings.pwm == 0 or CurrentSettings.pwm == -1:
          CurrentSettings.direction = FanData.direction
          print "Changing Direction of Fan"
       else:
         CurrentSettings.pwm = CurrentSettings.pwm - 1
         PWM.setpwm(CurrentSettings.pwm)
         print "Setting PWM to " + str(CurrentSettings.pwm) + " " + CurrentSettings.direction

  return CurrentSettings
