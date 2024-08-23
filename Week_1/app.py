# import pyowm

# owm = pyowm.OWM('{bf2a9fd0321fa9a5e53108e96bda0651}')

# mgr = owm.weather_manager()

# observation = mgr.weather_at_place('London,uk')

# w = observation.weather()

# print(w.get_wind())pip3 install -U wbdata

# 

from pprint import pprint

import requests



apikey = 'bf2a9fd0321fa9a5e53108e96bda0651'

try:
            location = input('Enter your Current Location: ').strip()
            
            if not location:
                raise ValueError("Location cannot be empty. Please enter a valid location.")
            
            elif not location.isalpha():
                raise ValueError("Location should only contain alphabetic characters. Please enter a valid location.")
            
except ValueError as ve:
            print(ve)
        



r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&APPID={apikey}')
  


response = r.json()


if response['cod'] == "404" :
    
    print("Invalid Location")
    
else:
    
    for key,value in response.items(): 
        
        print(f"{key}:  {value}")

