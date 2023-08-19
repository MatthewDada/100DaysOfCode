import requests
from twilio.rest import Client

# the api_key can be gotten from the openweathermap website
# the account_sid and auth_token can be gotten from twilio website

api_key = "41e3e748644f13a7c0c47ac78fd........"
Endpoint = "https://api.openweathermap.org/data/2.8/onecall"
account_sid = "AC707f3d379c6c2df2bb930ac........."
auth_token = "ec474db5b95c0dccc4603e4790........."

parameter = {
    "lat": -33.448891, # better to test with a location that's currently experiencing rainfall.
    "lon": -70.669266, # go to https://www.ventusky.com/ to see weather distribution across the world.
    "exclude": "current,minutely,daily",
    "appid": api_key

}

response = requests.get(Endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12] #to get only the weather condition for the next 12 hours.

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, remember to bring along an umbrella.",
        from_='+133....4085', #you'll have to generate a number on twilio website 
        to='+.....12703' #the number used to open the twilio account.
    )