import time
import RPi.GPIO as GPIO
import AccessWebServer
import PWM

PWM.setuppwm()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.output(15, GPIO.HIGH)

previousTime = time.time()
postTime = previousTime

def hallback(channel):
  global previousTime
  global postTime
  rpm = 60 / (time.time() - previousTime)
  print rpm

  if postTime - time.time() > 60:
    AccessWebServer.PostOp("Manual", rpm)
    postTime = time.time()
    
  previousTime = time.time()
  
GPIO.add_event_detect(11, GPIO.RISING, callback=hallback, bouncetime=55)

PWM.setpwm(22)

while True:
  time.sleep(.5)
