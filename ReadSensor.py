import Adafruit_ADS1x15 # Google search ADS1015/ADS1115 and follow adafruit tutorial
import time
import FanClass
import AccessWebServer

try:
  adc = Adafruit_ADS1x15.ADS1015()
except:
  print "Could not initalize the ADC"

tempData = FanClass.WeatherData(0.0, time.time())

def readTemp():
  GAIN = 4
  #tempCoef = 19.5    
  tempCoef = .01
  #voltAtZero = 400
  voltAtZero = .5
  global tempData

  if tempData.ElapsedTime() > 10 or tempData.data == 0.0:
    try:
      value = adc.read_adc(0, gain=GAIN)
      value = value * (1.024 / 2048.0)

      # Apply corrective function to attain temp value
      temp = (value - voltAtZero) / tempCoef

      # Convert from Celsius to Fahrenheit
      temp = (temp*(9.0/5.0)) + 32

      AccessWebServer.PostTemp(temp)

      tempData = FanClass.WeatherData(temp, time.time())

      return tempData.data

    except:
      print "Could not read ADC"
      return -3000
  else:
    return tempData.data
    
def readHumidity():
  GAIN = 1    

  try:
    value = adc.read_adc(1, gain=GAIN)

    # Apply corrective function to attain humidity value

    return humidity

  except:
    print "Could not read ADC"
    return -3000    

def readPotent():
  GAIN = 1

  try:
    value = adc.read_adc(0, gain=GAIN)
    potent = value * (30.0/2048.0) + 60
    return potent
  except:
    print "Could not read ADC"
    return -3000
