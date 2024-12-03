import requests

response = requests.get("https://www.alphavantage.co/")

# this gives a dict with prices
data = response.json()