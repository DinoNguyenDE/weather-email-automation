
import requests
import csv
import smtplib
from email.mine.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os 

def lay_thoi_tiet():   
    url = 'https://api.open-meteo.com/v1/forecast'
    params = {
        'latitude': 21.03,
        'longitude': 105.85,
        'daily': 'temperature_2m_max,temperature_2m_min,precipitation_sum',
        'timezone': 'Asia/Bangkok'
    }
    response = requests.get(url, params=params)
    daily = response.json()['daily']
    
    #chỉ lấy thời tiết hôm nay
    return {
        "location": "Hanoi",
        "date": daily['time'][0],
        "temperature_max": daily['temperature_2m_max'][0],
        "temperature_min": daily['temperature_2m_min'][0],
        "precipitation": daily['precipitation_sum'][0]
    }
    
def tao_noi_dung_email(thoi_tiet):
    noi_dung = f"""
    Thời tiết hôm nay tại {thoi_tiet['location']}:
    Ngày: {thoi_tiet['date']}
    Nhiệt độ cao nhất: {thoi_tiet['temperature_max']}°C
    Nhiệt độ thấp nhất: {thoi_tiet['temperature_min']}°C
    Lượng mưa: {thoi_tiet['precipitation']}mm
    """
    return noi_dung 

def gui_email(noi_dung):
    sender = os.environ.get('GMAIL_USER')
    password = os.environ.get('GMAIL_PASSWORD')
    receiver = os.environ.get('RECEIVER_EMAIL')
    
    msg = MIMEMultipart("alternative")
    msg['Subject'] = f"Bản tin thời tiết hôm nay"
    msg['From'] = sender
    msg['To'] = receiver
    msg.attach(MIMEText(noi_dung, 'html'))
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print("Email đã được gửi thành công!")
    
row = lay_thoi_tiet()
html = tao_noi_dung_email(row)
gui_email(html)