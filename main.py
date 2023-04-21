import requests
from datetime import datetime as dt
import time
import smtplib

# Define the latitude and longitude of your location
MY_LATITUDE = 47.430874
MY_LONGITUDE = 96.184269

# Set up sender email and password
MY_EMAIL = "sender_email"
MY_PASSWORD = "password"

# Check if the ISS is currently overhead
def is_overhead():
    # Make a request to the OpenNotify API to get the current location of the ISS
    response_overhead = requests.get(
        url="http://api.open-notify.org/iss-now.json")
    response_overhead.raise_for_status()
    data = response_overhead.json()
    # Get the latitude and longitude of the ISS from the response
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    # Check if the ISS is within 5 degrees of your location
    if MY_LATITUDE - 5 <= iss_latitude <= MY_LATITUDE + 5 and MY_LONGITUDE - 5 <= iss_longitude <= MY_LONGITUDE + 5:
        return True

# Check if it is currently night at your location
def is_night():
    # Make a request to the OpenWeatherMap API to get the current weather at your location
    url = "https://api.openweathermap.org/data/2.5/weather"
    querystring = {
        'q': "jaipur",
        'units': "metric",
        'appid': 'api_key'
    }
    response = requests.get(url, params=querystring)
    if response.status_code == 200:
        data = response.json()
        # Get the sunrise and sunset times for your location from the response
        sunrise_timestamp = data["sys"]["sunrise"]
        sunset_timestamp = data["sys"]["sunset"]
        # Convert the timestamps to hours
        sunrise_hour = dt.fromtimestamp(sunrise_timestamp).hour
        sunset_hour = dt.fromtimestamp(sunset_timestamp).hour
        # Get the current hour
        current_hour = dt.now().hour
        # Check if it is currently night (after sunset and before sunrise)
        if current_hour <= sunrise_hour or current_hour >= sunset_hour:
            return True
    else:
        print("Error getting weather data.")

# Run the program continuously, checking every minute if the ISS is overhead and it is night
while True:
    time.sleep(60)
    print("Checking for ISS...")
    if is_overhead() and is_night():
        # If the ISS is overhead and it is night, send an email
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs="receiver_email",
                                msg="Subject: LOOK UP!\n\nThe ISS is currently overhead at your location!")
            
            
#developed by bhimesh yadav
