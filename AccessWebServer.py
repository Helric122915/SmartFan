import requests
import json
import FanClass

PORTNUM = '3000'
url = 'http://130.101.94.161:' + PORTNUM

def GetOp():
  r = requests.get(url + '/GetOp')

  data = json.loads(r.text)
  opMode = data['data']

  return opMode

def PostOp(OpData):
  data = {}
  data["data"] = OpData

  r = requests.post(url + '/PostOp', data)
  print r.text

def GetManual():
  r = requests.get(url + '/GetManual')

  data = json.loads(r.text)
  manualData = FanClass.ManualData(data['data']['Manual_Direction'],int(data['data']['Manual_Fan_Speed']))

  return manualData

def PostManual(manualData):
  data = {}
  data["Manual_Direction"] = manualData.direction
  data["Manual_Fan_Speed"] = manualData.pwm
  
  r = requests.post(url + '/PostManual', data)
  print r.text

def GetOneTemp():
  r = requests.get(url + '/GetOneTemp')

  data = json.loads(r.text)
  oneTempData = FanClass.OneTempData(data['data']['One_Temp_Direction'],int(data['data']['One_Temp_Low_Speed']),int(data['data']['One_Temp_Low_Temp']),int(data['data']['One_Temp_High_Speed']),int(data['data']['One_Temp_High_Temp']))
  
  return oneTempData

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
  r = requests.get(url + '/GetTwoTemp')

  data = json.loads(r.text)
  twoTempData = FanClass.TwoTempData(int(data['data']['Two_Temp_Low_Speed']),int(data['data']['Two_Temp_Low_Temp']),int(data['data']['Two_Temp_High_Speed']),int(data['data']['Two_Temp_High_Temp']))

  return twoTempData

def PostTwoTemp(twoTempData):
  data = {}
  data["Two_Temp_Low_Speed"] = twoTempData.lowSpeed
  data["Two_Temp_Low_Temp"] = twoTempData.lowTemp
  data["Two_Temp_High_Speed"] = twoTempData.highSpeed
  data["Two_Temp_High_Temp"] = twoTempData.highTemp

  r = requests.post(url + '/PostTwoTemp', data)
  print r.text
