import Adafruit_ADS1x15 # Google search ADS1015/ADS1115 and follow adafruit tutorial

try:
  adc = Adafruit_ADS1x15.ADS1015()
except:
  print "Could not initalize the ADC"

def readTemp():
  GAIN = 1
  tempCoef = 19.5    
  voltAtZero = 400

  try:
    value = adc.read_adc(0, gain=GAIN)

    # Apply corrective function to attain temp value
    temp = (value - voltAtZero) / tempCoef

    # Convert from Celsius to Fahrenheit
    temp = (temp*(9.0/5.0)) + 32

    return temp

  except:
    print "Could not read ADC"
    return -3000
    
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
