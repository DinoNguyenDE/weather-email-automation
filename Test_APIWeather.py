import requests
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def lay_thoi_tiet():
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 21.03,
        "longitude": 105.85,
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
        "timezone": "Asia/Bangkok"
    }
    response = requests.get(url, params=params)
    daily = response.json()["daily"]
    return {
        "location": "Hà Nội",
        "date": daily["time"][0],
        "max_temp": daily["temperature_2m_max"][0],
        "min_temp": daily["temperature_2m_min"][0],
        "precipitation": daily["precipitation_sum"][0]
    }

def tao_noi_dung(row):
    return f"""
    <h2>🌤️ Thời tiết {row['location']} — {row['date']}</h2>
    <p>🌡️ Cao nhất: <b>{row['max_temp']}°C</b></p>
    <p>🌡️ Thấp nhất: <b>{row['min_temp']}°C</b></p>
    <p>🌧️ Lượng mưa: <b>{row['precipitation']} mm</b></p>
    """

def gui_email(noi_dung_html):
    sender   = os.environ.get("GMAIL_USER")
    password = os.environ.get("GMAIL_PASSWORD")
    receiver = os.environ.get("RECEIVER_EMAIL")

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Thời tiết Hà Nội hôm nay"
    msg["From"]    = sender
    msg["To"]      = receiver
    msg.attach(MIMEText(noi_dung_html, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
    print("Email đã được gửi thành công!")

row  = lay_thoi_tiet()
html = tao_noi_dung(row)
gui_email(html)