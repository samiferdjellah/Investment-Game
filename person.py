class Person:

    def __init__(self):
        self.firstName = ""
        self.lastName = ""
        
    def getFirstName(self):
        self.firstName = input("Please enter your first name: ")

    def getLastName(self):
        self.lastName = input("Please enter your last name: ")

    def getEmail(self):
        self.eMail = input("Please enter your e-mail address: ")

    def __str__(self):
        return f"Welcome {self.firstName} {self.lastName}."
