class ManualData(object):

  def __init__(self,direction,pwm):
    self.direction = direction
    self.pwm = pwm

class OneTempData(object):

  def __init__(self,direction,lowSpeed,lowTemp,highSpeed,highTemp):
    self.direction = direction
    self.lowSpeed = lowSpeed
    self.lowTemp = lowTemp
    self.highSpeed = highSpeed
    self.highTemp = highTemp

class TwoTempData(object):

  def __init__(self,lowSpeed,lowTemp,highSpeed,highTemp):
    self.lowSpeed = lowSpeed
    self.lowTemp = lowTemp
    self.highSpeed = highSpeed
    self.highTemp = highTemp

class CurrentFanData(object):

  def __init__(self,direction,pwm,power):
    self.direction = direction
    self.pwm = pwm
    self.power = power
