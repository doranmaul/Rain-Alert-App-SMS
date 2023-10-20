import requests
from twilio.rest import Client

account_sid = "TWILIO SID HERE"
auth_token = "TWILIO AUTH TOKEN HERE"

parameters = {
    "lat": LAT HERE,
    "lon": LONG HERE,
    "appid": "OWM API ID HERE",
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params=parameters)
response.raise_for_status()
data = response.json()

weather_id = data["weather"][0]["id"]

if weather_id <= 701:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Bring an umbrella.",
        from_='TWILIO NUMBER HERE',
        to='NUMBER TO SEND TO'
    )
    print(message.status)
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Keep an eye on the sky, but as of nigh, you should be dry.",
        from_='TWILIO NUMBER HERE',
        to='NUMBER TO SEND TO'
    )
    print(message.status)



