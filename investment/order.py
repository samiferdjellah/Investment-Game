
class Order:
  def __init__(self, name: str, type: str, quantity: int, stockValue: float, total: float):
    self.name = name
    self.type = type
    self.quantity = quantity
    self.stockValue = stockValue
    self.total = total
    
  # def add_stock(self, ):
  
  def calculateTotal(self, quantity: int, price: float) -> None:
    self.total = quantity * price
    
  def __str__(self) -> str:
    return f"name: {self.name}\nquantity: {self.quantity}\ntype: {self.type}\nstock price: {self.stockValue}\ntotal: {self.total}"
  
    
    