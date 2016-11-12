import requests
import json
import FanClass

url = 'http://130.101.94.161'

def GetCurrentFanData():
  r = requests.get(url + '/CurrentFanData')

  json_test = json.loads(r.text)
  fanData = FanClass.FanData(int(json_test['Class']['Fan_Speed']),int(json_test['Class']['Room_Temp']))

  return fanData

#print "Print Original Web Server Info"
#print r.text
#print json_test
#print json_test['Class']['Room_Temp']
#print json_test['Class']['Fan_Speed']
#print fanData.roomTemp
#print fanData.fanSpeed

#fanData = FanClass.FanData(3600, 73)

def PostUpdateFanData(fanData):
  data = {}
  data["Room_Temp"] = fanData.roomTemp
  data["Fan_Speed"] = fanData.fanSpeed
  json_data = json.dumps(data)

  r = requests.post(url + '/UpdateFanData', data)
  print r.text
