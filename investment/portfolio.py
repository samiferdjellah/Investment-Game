from investment.person import Person
from investment.order import Order

class Portfolio:
  def __init__(self, person: Person, orders: list[Order], balance: float):
    self.person = person
    self.orders = orders
    self.balance = balance
    
  def add_order(self, order: Order):
    self.orders.append(order)
    
  def __str__(self) -> str:
    orders = ""
    f"{self.person} has following stocks in his portfolio:\n"
    for order in self.orders:
      orders += order.__str__() + "\n"
    return orders