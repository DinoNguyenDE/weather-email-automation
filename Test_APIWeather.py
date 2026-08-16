

import requests
import csv


url = 'https://api.open-meteo.com/v1/forecast'
params = {
    'latitude': 21.03,
    'longitude': 105.85,
    'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
    'timezone': 'Asia/Bangkok'
}
response = requests.get(url, params=params)
data = response.json()
rows = []

for time, temp_max, temp_min, sum_precipitation in zip( data['daily']['time'], 
                                                       data['daily']['temperature_2m_max'],
                                                       data['daily']['temperature_2m_min'],
                                                       data['daily']['precipitation_sum']):
    rows.append({
        "location": 'hanoi',
        "date": time,
        "max_temperature": temp_max,
        "min_temperature": temp_min,
        "precipitation": sum_precipitation
})

with open('weather_data.csv', 'w', newline='', encoding='utf-8-sig') as f:
    writer = csv.DictWriter(f, fieldnames=['location', 'date', 'max_temperature', 'min_temperature', 'precipitation'])
    writer.writeheader()
    writer.writerows(rows)
print(f"Đã lưu {len(rows)} ngày dữ liệu thời tiết vào file weather_data.csv")   