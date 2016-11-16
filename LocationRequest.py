import requests
import json
import time

class ReturnValue(object):
  def __init__(self, lat,lng):
    self.lat = lat
    self.lng = lng

api_url = "https://maps.googleapis.com/maps/api/geocode/json?address="
api_key = "&key=AIzaSyBJJXI_obzn3EXqjfZ5EtaVrWTZTBGqj3c"

def LatLng(address):
  address = address.replace(" ","+")
  query_url = api_url + address + api_key

  r = requests.get(query_url)

  if r.status_code != 200:
    print "Error:", r.status_code
  else: 
    print r
    json_weather = r.json()
    lat =  json_weather['results'][0]['geometry']['bounds']['northeast']['lat']
    lng = json_weather['results'][0]['geometry']['bounds']['northeast']['lng']
    
    # Fix these two JSON object access methods because Google appears to randomly change the structure
    
    return ReturnValue(lat, lng)


  #if r.status_code != 200:
   # print "Error:", r.status_code
  #else:
   # json_weather = r.json()
   # return json_weather

#def CurrentTemp(lat = 41.07472, long = -81.52201):
 # json_weather = Current(lat, long)

  #return json_weather['currently']['temperature']


#print json_weather
#print "\n"

#currentTime = json_weather['currently']['time']

#currentTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(currentTime))

#print currentTime

#currentTemp = json_weather['currently']['temperature']

#print "The Current Temperature is: "  + str(currentTemp) + " Fahrenheit"

#currentWeather = json_weather['currently']['icon']

#if "cloud" in currentWeather:
#	print "Currently it is: Cloudy"
#elif "rain" in currentWeather:
#	print "Currently it is: Raining"
#else:
#	print "Currently it is: Clear"

#nearestStorm = json_weather['currently']['nearestStormDistance']

#print "The nearest Storm is " + str(nearestStorm) + " Kilometer(s) away."
