import requests
from twilio.rest import Client
from config import OWM_API_KEY, TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = OWM_API_KEY
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN

weather_params = {
    "lat": 30.267153,
    "lon": -97.743057,
    "appid" : api_key,
    "cnt" : 4,
}


response = requests.get(OWM_ENDPOINT, params=weather_params)
print(response)
response.raise_for_status()
print(response.status_code)
weather_data = response.json()
#print(weather_data["list"][0]["weather"]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="whatsapp:+14155238886",
        body="It's going to rain today. Remember to bring an umbrella",
        to="whatsapp:+919848508577"
    )
    # message = client.messages \
    #     .create(
    #     body="It's going to rain today. Remember to bring an ☂️.",
    #     to="+919848508577",
    #     from_="+17406608259",
    # )
    print(message.status)