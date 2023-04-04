import requests
from datetime import datetime
import smtplib
import time

EMAIL = "iss-overheader-notification@gmail.com"
PASSWORD = "nasasasamasa()"
LATITUDE = 51.507351
LONGITUDE = -0.127758

def is_iss_overhead():
    response = requests.get(url= "http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()["iss_position"]
    latitude = float(data["latitude"])
    longitude = float(data["longitude"])
    if LATITUDE-5 <= latitude <= LATITUDE+5 and LONGITUDE-5 <= longitude <= LONGITUDE+5:
        return True

def is_dark():
    parameters = {
        "lat": LATITUDE,
        "lng": LONGITUDE,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    current_time = datetime.now().hour
    if current_time >= sunset or current_time <= sunrise:
        return True

while True
    time.sleep(60)
    if is_iss_overhead() and is_dark():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(from_addr= EMAIL, to_addrs= EMAIL, msg="Subject:ISS above you!\n\nGoodNewz!\nSpot ISS above you NOW!")
        connection.close()