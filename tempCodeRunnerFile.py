import requests
city_name="mumbai"
data =requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid=daa9c2c6d17f8f008933b1b4b5b13a7f").json()
print(data)