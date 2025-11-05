import requests 
import pandas as pd
import matplotlib.pyplot as plt



from datetime import datetime, timedelta
today = datetime.now()
week_ago = today -timedelta(days=7)

start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
latitude= 26.84
longitude= 80.94
url =f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response= requests.get(url)
data=response.json()
print(data)

#____________________using pandas______________________
daily_data = data['daily']
print(daily_data)
df = pd.DataFrame({
    "date":daily_data["time"],
    "max_temp":daily_data["temperature_2m_max"],
    "min_temp":daily_data["temperature_2m_min"]
})
df["date"]=pd.to_datetime(df["date"])

print(df)
#__--using matlplotlib____________--

plt.figure(figsize=(10,6))
#x axis
plt.plot(df["date"],df["max_temp"], marker='o', label="Max_temp")
# y axis
plt.plot(df["date"],df["min_temp"], marker='o', label="Min_temp")
# name x axis

plt.xlabel("Date")
#name y axis
plt.ylabel("Temperature (C)")
#title of graph
plt.title("Lucknow weather -Past 7 days")
#Displays the legend box using labels you defined earlier (label='Max Temp' etc).
plt.legend()
#Rotates the date labels on the x-axis 45 degrees,
plt.xticks(rotation=45)
#Automatically adjusts spacing in the figure to make sure labels and titles fit well within the window —

plt.tight_layout()
plt.savefig('weather-chart.png')
plt.show()
