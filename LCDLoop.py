import time
import AccessWebServer
import LCDcontrol as lcd

message = ""
previousTime = time.time()
currentlyOn = False

while True:
  previousMessage = message
  message = AccessWebServer.GetMessage()

  if message != previousMessage:
    lcd.setBacklight(0)
    lcd.writeClear(message)
    previousTime = time.time()
    currentlyOn = True
  elif (time.time() - previousTime > 10) and currentlyOn:
    lcd.setBacklight(1)
    lcd.clear()
    currentlyOn = False
    
  time.sleep(.5)

