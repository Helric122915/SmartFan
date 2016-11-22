class FanData(object):

  def __init__(self,fanSpeed,roomTemp):
    # General Variables
    self.roomTemp = roomTemp
    self.fanOff = fanOff
    self.direction = direction

    # Manual Mode Variables
    self.manualModeFanSpeed = fanSpeed
    
    # Schedule Mode Variables
    # What variables do we need to support this mode?

    # One Source Temp Mode Variables
    self.oneTempLowTemp = oneTempLowTemp
    self.oneTempLowSpeed = oneTempLowSpeed
    self.oneTempHighTemp = oneTempHighTemp
    self.oneTempHighSpeed = oneTempHighSpeed

    # Two Source Temp Mode Variables
    self.twoTempLowTemp = twoTempLowTemp
    self.twoTempLowSpeed = twoTempLowSpeed
    self.twoTempHighTemp = twoTempHighTemp
    self.twoTempHighSpeed = twoTempHighSpeed
