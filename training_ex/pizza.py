class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return self.name


class Pizza:
    base_price = 5
    def __init__(self, name, toppings):
        self.name = name
        self.toppings = toppings

    def price(self):
        # your code here
        self.base_price

# Example of using the pizza class
if __name__ == "__main__":
    p = Pizza("Margherita", [Topping("Cheese", 1), Topping("Tomato", 0.5)])
    print(p)
    print(p.price())