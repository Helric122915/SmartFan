# Jacob is a butt

import wiringpi # Requires "pip install wiringpi"

def setuppwm():
    wiringpi.wiringPiSetup()
  
def setpwm(pwm):
    OUTPUT = 2
    TURN_OFF = 0
    PIN_TO_PWM = 1 # GPIO 18 on the RPI
  
    if pwm == -1:
        wiringpi.pinMode(PIN_TO_PWM, TURN_OFF)
        result = True
  
    elif pwm >= 0 and pwm <= 2023:
        wiringpi.pinMode(PIN_TO_PWM, OUTPUT)
        wiringpi.pwmWrite(PIN_TO_PWM, pwm)
        result = True
    
    else:
        result = False
  
    return result
