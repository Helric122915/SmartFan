class FanData(object):

  def __init__(self,opMode,direction,manualModeFanSpeed):
    # General Variables
    self.opMode = opMode #Manual,OneTemp,TwoTemp,Schedule
    self.direction = direction

    # Manual Mode Variables
    self.manualModeFanSpeed = manualModeFanSpeed
    
    # Schedule Mode Variables
    # What variables do we need to support this mode?
    # I believe we will need a list of time intervals to support this mode
    # The schedule mode will search through the list of intervals
    # to check if the fan should currently be on and at which rate
    # the fan should operate at.    

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
                      # just changed the order of pwm and direction will mess up calls to this class
  def __init__(self,direction,pwm,power):
    self.direction = direction
    self.pwm = pwm
    self.power = power
