import requests
from dotenv import load_dotenv
import os
import smtplib
from email.message import EmailMessage

load_dotenv()

API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

print("API Key:", API_KEY)
print("City:", CITY)

url = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(url)
data = response.json()
if data["cod"] == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("Temperature:", temp, "°C")
    print("Weather:", weather)

    if data["cod"] == 200:
        temp = data["main"]["temp"]
        weather = data["weather"][0]["description"]

    print("Temperature:", temp, "°C")
    print("Weather:", weather)

    if "rain" in weather.lower() or "drizzle" in weather.lower():
        print("⚠ Rain Alert!")

        msg = EmailMessage()
        msg["Subject"] = "Rain Alert!"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        msg.set_content(
            f"Rain expected in {CITY}.\nTemperature: {temp} °C\nWeather: {weather}"
        )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
            smtp.send_message(msg)

        print("📧 Email sent!")

    else:
        print("✅ No rain expected")

else:
    print("Error:", data)