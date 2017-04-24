import time

class LocationData(object):

  def __init__(self,latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude

class WeatherData(object):

  def __init__(self,data,accessTime):
    self.data = data
    self.accessTime = accessTime

  def ElapsedTime(self):
    return time.time() - self.accessTime

class FanStatus(object):

  def __init__(self,mode,power,rpm):
    self.mode = mode
    self.power = power
    self.rpm = rpm
    
class ManualData(object):

  def __init__(self,direction,pwm):
    self.direction = direction
    self.pwm = pwm

class ScheduleData(object):

  def __init__(self,direction,pwm):
    self.direction = direction
    self.pwm = pwm

class OneTempData(object):

  def __init__(self,direction,lowSpeed,lowTemp,highSpeed,highTemp,pwm=-1):
    self.pwm = pwm
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

  def __init__(self,direction,pwm,mode='N/A',differential='N/A'):
    self.direction = direction
    self.pwm = pwm
    self.mode = mode
    self.differential = differential
