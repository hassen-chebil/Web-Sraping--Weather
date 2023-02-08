# -*- coding: utf-8 -*-
"""Weather-city.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13i2JG4a-7stdcfHW0d_SHaRklW1TYNoX
"""





# import required modules (requests module is used for making HTTP requests / json module is used for handling json data )
import requests, json 

# Enter your API key here 
api_key = "b8e909c7c126a848d7d7ea55ceeeeaad"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
City_départ = input("Enter city name : ") 


# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + City_départ +"&units=metric"

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 

# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

	# store the value of "main" 
	# key in variable y 
	y = x["main"] 

	# store the value corresponding 
	# to the "temp" key of y 
	current_temperature = y["temp"] 

	# store the value corresponding 
	# to the "pressure" key of y 
	current_pressure = y["pressure"] 

	# store the value corresponding 
	# to the "humidity" key of y 
	current_humidiy = y["humidity"] 

	# store the value of "weather" 
	# key in variable z 
	z = x["weather"] 

	# store the value corresponding 
	# to the "description" key at 
	# the 0th index of z 
	weather_description = z[0]["description"] 

	# print following values 
	print(" Temperature (in celsius unit) = " +
					str(current_temperature) +
		"\n atmospheric pressure (in hPa unit) = " +
					str(current_pressure) +
		"\n humidity (in percentage) = " +
					str(current_humidiy) +
		"\n description = " +
					str(weather_description)) 

else: 
	print(" City Not Found ") 
    
token="ed3ef39e4c5c17545c45a711195855c8029a3c99"
base_url2 = "https://api.waqi.info/feed/"
complete_url2 = base_url2+City_départ+"/"+ "?token="+token
response2 = requests.get(complete_url2) 
x2 = response2.json() 

try:
    aqi=x2['data']['aqi']
    print(aqi)
    if (aqi in range(50)):
        print("Niveau de pollution de l'air est Bon")
    if (aqi in range(51,101)):
        print("Niveau de pollution de l'air est Modéré")
    if (aqi in range(101,151)):
       print("Niveau de pollution de l'air est Mauvais pour les groupes sensibles")
    if (aqi in range(151,201)):
       print("Niveau de pollution de l'air est Mauvais")
    if (aqi in range(201,301)):
       print("Niveau de pollution de l'air est Très mauvais")
    if (aqi>300):
        print("Niveau de pollution de l'air est Dangereux")
except:
    results=requests.get("https://api.weatherbit.io/v2.0/current?city={}&key=0fb922cfedb6437a96182967cca3668f".format(City_départ))
    results1=results.json()

    with open('weather3.json', 'w') as outfile:
        json.dump(results1, outfile)
    
        aqi1=results1['data'][0]['aqi']
        if (aqi1 in range(50)):
           print("Niveau de pollution de l'air est Bon")
        if (aqi1 in range(51,101)):
            print("Niveau de pollution de l'air est Modéré")
        if (aqi1 in range(101,151)):
            print("Niveau de pollution de l'air est Mauvais pour les groupes sensibles")
        if (aqi1 in range(151,201)):
             print("Niveau de pollution de l'air est Mauvais")
        if (aqi1 in range(201,301)):
             print("Niveau de pollution de l'air est Très mauvais")
        if (aqi1>300):
              print("Niveau de pollution de l'air est Dangereux")









