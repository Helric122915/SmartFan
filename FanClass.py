import time

class LocationData(object):

  def __init__(self,latitude,longitude):
    self.latitude = latitude
    self.longitude = longitude

class WeatherData(object):

  def __init__(self,json,accessTime):
    self.json = json
    self.accessTime = accessTime

  def ElapsedTime(self):
    return time.time() - self.accessTime

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

  def __init__(self,direction,pwm,power,mode='N/A',differential='N/A'):
    self.direction = direction
    self.pwm = pwm
    self.power = power
    self.mode = mode
    self.differential = differential
