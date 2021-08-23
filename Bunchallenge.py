#imports
import requests, json
<<<<<<< HEAD
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
=======
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
>>>>>>> 59ad4017bae60c66065f1c0d8996068d695b2120
