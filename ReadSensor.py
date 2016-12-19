import Adafruit_ADS1x15 # Google search ADS1015/ADS1115 and follow adafruit tutorial

def readTemp()
    adc = Adafruit_ADS1x15.ADS1015()
    GAIN = 1
    tempCoef = 19.5    
    voltAtZero = 400

    value = adc.read_adc(0, gain=GAIN)
    
    # Apply corrective function to attain temp value
    temp = (value - voltAtZero) / tempCoef    

    # Convert from Celsius to Fahrenheit
    temp = (temp*(9.0/5.0)) + 32

    return temp
    
def readHumidity()
    adc = Adafruit_ADS1x15.ADS1015()
    GAIN = 1
    
    value = adc.read_adc(1, gain=GAIN)
    
    # Apply corrective function to attain humidity value
    
    return humidity
