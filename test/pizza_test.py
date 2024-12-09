from pizza import Topping, Pizza

def test_price_one():
  pizza = Pizza("test", [])
  result = pizza.price()
  assert result == 0
  
def test_price_two():
  pizza = Pizza("test", [Topping("Cheese")])
  result = pizza.price()
  assert result == 1
  
def test_price_three():
  pizza = Pizza("test", [Topping("Cheese")], Topping("tomato"))
  result = pizza.price()
  assert result == 1
  
def test_price_wrong():
  pizza = Pizza(5, [Topping("Cheese")])
  result = pizza.price()
  assert result == 
  