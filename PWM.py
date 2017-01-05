import wiringpi # Requires installing from the WiringPi/WiringPi-Python wrapper class

def setuppwm():
    wiringpi.wiringPiSetup()

def configurepwm():
    wiringpi.pwmSetMode(wiringpi.PWM_MODE_MS)
    wiringpi.pwmSetClock(10)
    wiringpi.pwmSetRange(48)  

def setpwm(pwm):
    OUTPUT = 2
    TURN_OFF = 0
    PIN_TO_PWM = 1 # GPIO 18 on the RPI
  
    if pwm == -1:
        wiringpi.pinMode(PIN_TO_PWM, TURN_OFF)
        result = True

    # The PWM value can be between 0 and 48 ranging from 0 to ~3.3 volts  
    elif pwm >= 0 and pwm <= 49:
        wiringpi.pinMode(PIN_TO_PWM, OUTPUT)
        configurepwm()
        wiringpi.pwmWrite(PIN_TO_PWM, pwm)
        result = True
    
    else:
        result = False
  
    return result
