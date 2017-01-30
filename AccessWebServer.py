import requests
import json
import FanClass
import time

PORTNUM = '3000'
url = 'http://130.101.95.132:' + PORTNUM

def GetOp():
  try:
    r = requests.get(url + '/GetOp')

    if r.status_code != 200:
      print "Error:", r_status_code
      return "NoMode"
    else:
      data = json.loads(r.text)
      opMode = data['data']['Mode']

      return opMode
  
  except:
    return "NoMode";

def PostOp(OpData):
  data = {}
  data["Mode"] = OpData

  r = requests.post(url + '/PostOp', data)
  print r.text

def GetAddress():
  try:
    r = requests.get(url + '/GetAddress')

    if r.status_code != 200:
      print "Error:", r.status_code
      return FanClass.LocationData(0,0)
    else:
      data = json.loads(r.text)
      locationData = FanClass.LocationData(data['data']['Latitude'],data['data']['Longitude'])

      return locationData

  except:
    return FanClass.LocationData(0,0)
    

def GetManual():
  try:
    r = requests.get(url + '/GetManual')

    if r.status_code != 200:
      print "Error:", r.status_code
      return FanClass.ManualData('N/A',-1)
    else:
      data = json.loads(r.text)
      manualData = FanClass.ManualData(data['data']['Manual_Direction'],int(data['data']['Manual_Fan_Speed']))

      return manualData

  except:
    return FanClass.ManualData('N/A',-1)

def PostManual(manualData):
  data = {}
  data["Manual_Direction"] = manualData.direction
  data["Manual_Fan_Speed"] = manualData.pwm
  
  r = requests.post(url + '/PostManual', data)
  print r.text

def GetCurrentSchedule():
  try:
    r = requests.get(url + '/GetCurrentSchedule')

    if r.status_code != 200:
      print "Error:", r.status_code
      return FanClass.ScheduleData('N/A',-1)
    else:
      data = json.loads(r.text)
      scheduleData = FanClass.ScheduleData(data['data']['Direction'],data['data']['Fan_Speed'])
    
      return scheduleData
  
  except:  
    return FanClass.ScheduleData('N/A',-1)

def GetOneTemp():
  try:
    r = requests.get(url + '/GetOneTemp')

    if r.status_code != 200:
      print "Error:", r.status_code
      return FanClass.OneTempData('N/A',0,0,0,0)
    else:
      data = json.loads(r.text)
      oneTempData = FanClass.OneTempData(data['data']['One_Temp_Direction'],int(data['data']['One_Temp_Low_Speed']),int(data['data']['One_Temp_Low_Temp']),int(data['data']['One_Temp_High_Speed']),int(data['data']['One_Temp_High_Temp']))
  
      return oneTempData

  except:
    return FanClass.OneTempData('N/A',0,0,0,0)

def PostOneTemp(oneTempData):
  data = {}
  data["One_Temp_Direction"] = oneTempData.direction
  data["One_Temp_Low_Speed"] = oneTempData.lowSpeed
  data["One_Temp_Low_Temp"] = oneTempData.lowTemp
  data["One_Temp_High_Speed"] = oneTempData.highSpeed
  data["One_Temp_High_Temp"] = oneTempData.highTemp
  
  r = requests.post(url + '/PostOneTemp', data)
  print r.text

def GetTwoTemp():
  try:
    r = requests.get(url + '/GetTwoTemp')

    if r.status_code != 200:
      print "Error:", r.status_code
      return FanClass.TwoTempData(0,0,0,0)
    else:
      data = json.loads(r.text)
      twoTempData = FanClass.TwoTempData(int(data['data']['Two_Temp_Low_Speed']),int(data['data']['Two_Temp_Low_Temp']),int(data['data']['Two_Temp_High_Speed']),int(data['data']['Two_Temp_High_Temp']))

      return twoTempData

  except:
    return FanClass.TwoTempData(0,0,0,0)

def PostTwoTemp(twoTempData):
  data = {}
  data["Two_Temp_Low_Speed"] = twoTempData.lowSpeed
  data["Two_Temp_Low_Temp"] = twoTempData.lowTemp
  data["Two_Temp_High_Speed"] = twoTempData.highSpeed
  data["Two_Temp_High_Temp"] = twoTempData.highTemp

  r = requests.post(url + '/PostTwoTemp', data)
  print r.text
