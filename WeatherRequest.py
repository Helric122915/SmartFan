import requests
import json
import time
import LocationRequest
import AccessWebServer
import FanClass

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

def Current():
  locationData = AccessWebServer.GetAddress()

  if locationData.latitude == 0 or locationData.longitude == 0:
    locationData.latitude = 41.076029
    locationData.longitude = -81.502305
 
  query_url = api_url % (api_key, locationData.latitude, locationData.longitude)
  r = requests.get(query_url);

  if r.status_code != 200:
    print "Error:", r.status_code
  else:
    json_weather = r.json()
    #print "API Query"
    return json_weather

weatherData = FanClass.WeatherData(Current(), time.time())

def WeatherData():
  global weatherData
  if weatherData.ElapsedTime() > 300:
    weatherData = FanClass.WeatherData(Current(), time.time())
  
  return weatherData.json

def CurrentTemp():
  json_weather = WeatherData()

  # Temporarily adding 55.0 to make the temperature more appropriate.
  return float(json_weather['currently']['temperature']) + 55.0

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
