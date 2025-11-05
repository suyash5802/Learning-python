import requests

longitude=2.35  
latitude=48.85

url=f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
response=requests.get(url)
data=response.json()
print(data["current"]["temperature_2m"])
