#-*- coding: utf-8 -*-

import LocationRequest
import WeatherRequest
import PWM
import time
import FanClass
import AccessWebServer
import ReadSensor
import LCDcontrol as lcd

import gaugette.rotary_encoder as rotary
#import gaugette.switch as switch

A_PIN = 28
#A_PIN = 29
B_PIN = 26
#B_PIN = 37
#SW_PIN = 8

encoder = rotary.RotaryEncoder.Worker(A_PIN, B_PIN)
encoder.start()
#switch = switch.Switch(SW_PIN)
#last_state = None

manualData = AccessWebServer.GetManual()

pwm = manualData.pwm

while True:
  delta = encoder.get_delta() / 4.0
  
  if delta != 0:
    if (pwm + delta) > 49:
      pwm = 49
    elif (pwm + delta) < 0:
      pwm = 0
    else:
      pwm = pwm + delta
    manualData = AccessWebServer.GetManual()
    manualData.pwm = pwm
    AccessWebServer.PostManual(manualData)

  #print ReadSensor.readTemp()
  #print "pwm %d" % pwm
  time.sleep(1)

  #else:
  #  print delta
  #time.sleep(1)

 # sw_state = switch.get_state()
 # if sw_sate != last_state:
 #   print "switch %d" % sw_state
 #   last_state = sw_state

#text = u'\u9608'

#print WeatherRequest.Current()

#WeatherRequest.WeatherData("ello")
#time.sleep(10)
#WeatherRequest.WeatherData("sup")

#while True:
#  print WeatherRequest.CurrentTemp()
  #WeatherRequest.WeatherData()
#  time.sleep(2)

#WeatherRequest.GetLastAccess("Hello")

#print WeatherRequest.ElapsedTime()

#opMode = AccessWebServer.GetOp();
#print opMode.mode
#print opMode.power

#scheduleData = AccessWebServer.GetCurrentSchedule();

#print str(scheduleData.beginTime.tm_hour)+":"+str(scheduleData.beginTime.tm_min)+":"+str(scheduleData.beginTime.tm_sec);
#print str(scheduleData.endTime.tm_hour)+":"+str(scheduleData.endTime.tm_min)+":"+str(scheduleData.endTime.tm_sec);
#print scheduleData.direction
#print scheduleData.pwm
#lcd.setBacklight(0)

#lcd.writeMessage('Jacob is\nDumb')
#lcd.writeMessage('Fan Speed\n')
#lcd.writeMessage('PWM set to 27')
#lcd.writeMessage(u'\u0031')
#lcd.createChar(1,[0x0,0x8,0xc,0xe,0xc,0x8,0x0,0x0])
#lcd.createChar(2,[0x0,0x2,0x6,0xe,0x6,0x2,0x0,0x0])
#lcd.write8(31)
#time.sleep(7)
#lcd.writeMessage('\x01')

#while True:
# temp = ReadSensor.readTemp()
# lcd.writeClear(str(temp))
  #lcd.clear()
  #lcd.writeMessage('Backlight On')
  #lcd.setBacklight(0)
# time.sleep(2)

  #lcd.clear()
  #lcd.writeMessage('Backlight Off')
  #lcd.setBacklight(1)
  #time.sleep(2)

#manualData = FanClass.ManualData("Counterclockwise",43)
#twoTempData = AccessWebServer.GetTwoTemp()

#twoTempData.lowSpeed = 7

#AccessWebServer.PostTwoTemp(twoTempData)

#AccessWebServer.PostManual(manualData)

#while True:
 # value = ReadSensor.readPotent()
  #print value
  #time.sleep(1)

#PWM.setuppwm()

#PWM.setpwm(20)

#count = -1

#while count < 49:
#  PWM.setpwm(count)
  
#  print "PWM set to: " + str(count)

#  count = count + 1
  
#  time.sleep(10)


#val = LocationRequest.LatLng("70 Wise Street, Akron, OH")

#print WeatherRequest.CurrentAddress("70 Wise Street, Akron, OH")

#print WeatherRequest.CurrentTemp(val.lat, val.lng)

#print val.lat
#print val.lng
