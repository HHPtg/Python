#imports
import requests, json
#user input
city_name = input("Enter city/Country name : ") 
#url_base
base_url = "http://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=d63af4c2b637eccb56f846d82d6c742f" 
#processing
response = requests.get(base_url) 
weather_json = response.json()
if weather_json["cod"] != "404": 
    y = weather_json["main"] 
current_temperature = y["temp"]
#output/print
c = current_temperature-273.15
print ("Temperature in °C = " + str(c)+"°" )
