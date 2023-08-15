import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 0 # Replace with your values.
MY_LONG = 0

MY_PASSWORD = ""
MY_EMAIL = "email@gmail.com"
RECIPIENT_EMAIL = "email@gmail.com"


def iss_within_range():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.

    if ((5 >= MY_LAT - iss_latitude > 0) or (5 >= iss_latitude - MY_LAT > 0)) and (
            (5 >= MY_LONG - iss_longitude > 0) or (5 >= iss_longitude - MY_LONG > 0)):
        return True


def is_nighttime():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60) # So that it runs every minute
    if iss_within_range() and is_nighttime():
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as connection:
            connection.ehlo()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECIPIENT_EMAIL,
                                msg="Subject:ISS Within Range!.\n\nThe ISS is above you. Look up in the sky")

