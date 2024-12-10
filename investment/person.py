class Person:

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName
        
    # def getFirstName(self):
    #     self.firstName = input("Please enter your first name: ")

    # def getLastName(self):
    #     self.lastName = input("Please enter your last name: ")

    # def getEmail(self):
    #     self.eMail = input("Please enter your e-mail address: ")
        
    # def add_to_balance(self, value: float) -> None:
    #     self.balance += value 

    def __str__(self):
        return f"{self.firstName} {self.lastName}"
