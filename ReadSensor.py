import Adafruit_ADS1x15 # Lookup required command to install this

def readTemp()
    adc = Adafruit_ADS1x15.ADS1015()
    GAIN = 1
    
    value = adc.read_adc(0, gain=GAIN)
    
    # Apply corrective function to attain temp value
    
    return temp
    
def readHumidity()
    adc = Adafruit_ADS1x15.ADS1015()
    GAIN = 1
    
    value = adc.read_adc(1, gain=GAIN)
    
    # Apply corrective function to attain humidity value
    
    return humidity
