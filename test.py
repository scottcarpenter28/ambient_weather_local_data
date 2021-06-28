"""
Just a class to test connections and things
"""
import requests
from dotenv import load_dotenv
import os

# Require api_key, application_key, and mac if more than one device
load_dotenv()

api_key = os.environ.get("API_KEY", None)
application_key = os.environ.get("APPLICATION_KEY", None)
device_mac = os.environ.get("DEVICE_MAC", None)

# https request for json data
url_request = "https://api.ambientweather.net/v1/devices?apiKey=%s&applicationKey=%s&devices=%s" % \
              (api_key,
               application_key,
               device_mac)

# list[dict] of recent data
recent_data = requests.get(url=url_request).json()
try:
    recent_data = recent_data[0]["lastData"]
except IndexError:
    exit("Index out of range")


print(recent_data)
