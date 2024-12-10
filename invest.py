import requests
from investment.order import Order
from investment.portfolio import Portfolio
from investment.person import Person 

firstName = input("Please enter your name: ")
lastName = input("Please enter your last name: ")
person = Person(firstName, lastName)
orderType = input("What do you want to do, buy(b) or sell(s) stocks?")

if orderType == "s":
    print("selling stocks")
elif orderType == "o":
    print("order stocks")

order = Order(None, type, None, None, None)
response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo", verify=False)
                        
data = response.json()
print(data)
latest = list(data["Time Series (5min)"].keys())[0]
latestOpen = data["Time Series (5min)"][latest]['1. open']

name = input("Please enter the name of the stock you want to place an order for: ")
order.name = name
quantity = int(input("Enter the amount of stocks you want: "))
order.quantity = quantity
order.stockValue = float(latestOpen)
order.calculateTotal(quantity, latestOpen)

portfolio = Portfolio(person, [], 0)
portfolio.add_order(order)

print(f"{person}, your portfolio consists of following stocks: {portfolio}" )