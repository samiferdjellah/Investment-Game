import requests

response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=53HU7S3992V5RPQZ", verify=False)
data = response.json()
print(data)