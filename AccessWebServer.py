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

def GetManual():
  r = requests.get(url + '/GetManual')

  data = json.loads(r.text)
  manualData = FanClass.ManualData(data['data']['Manual_Direction'],int(data['data']['Manual_Fan_Speed']))

  return manualData

def PostManual(manualData):
  data = {}
  data["Manual_Direction"] = manualData.direction
  data["Manual_Fan_Speed"] = manualData.pwm
  json_data = json.dumps(data)

  r = requests.post(url + '/PostManual', data)
  print r.text
