import requests
import json
import time
import LocationRequest

api_url = "https://api.darksky.net/forecast/%s/%f,%f"
api_key = "9c1f7351528fc58f40881d5bf2651719"

def CurrentAddress(address):
  location = LocationRequest.LatLng(address)

  weather = Current(location.lat, location.lng)
  return weather

def CurrentTempAddress(address):
  location = LocationRequest.LatLng(address)

  temp = CurrentTemp(location.lat, location.lng)
  return temp

def Current(lat = 41.07472, lng = -81.52201):
  query_url = api_url % (api_key, int(float(lat)), int(float(lng)))
  r = requests.get(query_url)

  if r.status_code != 200:
    print "Error:", r.status_code
  else:
    json_weather = r.json()
    print json_weather
    return json_weather

def CurrentTemp(lat = 41.07472, long = -81.52201):
  json_weather = Current(lat, long)

  return json_weather['currently']['temperature']


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
