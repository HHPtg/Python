#imports
import requests, json
#recursion
def restart():
    city_name = input("Enter city/Country name : ") 
    base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=d63af4c2b637eccb56f846d82d6c742f" 
    response = requests.get(base_url) 
    weather_json = response.json()
    if weather_json["cod"] != "404":
     y = weather_json["main"] 
     current_temperature = y["temp"]
     c = current_temperature-273.15
     print ("Temperature in °C = " + str(c)+"°" )
     restart()
restart()
