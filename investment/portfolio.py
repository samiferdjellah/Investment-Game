from person import Person
from order import Order

class Portfolio:
  def __init__(self, person: Person, stocks: list[Order], balance: float):
    self.person = person
    self.stocks = stocks
    self.balance = balance
    
  def add_order(self, order: Order):
    self.stocks.append(order)
    
  def __str__(self) -> str:
    