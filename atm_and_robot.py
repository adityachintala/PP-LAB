"""
Write the following classes with class variables, instance variable and illustration the self variable
i) Robot (to greet the world)
ii) ATM (to deposit and withdraw amount from ATM machine)
"""


class ATM:
    balance = 0

    def __init__(self, amount):
        self.balance = amount

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance


class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Robot says hello to", self.name)


# Robot
str = input("Enter your name:")
r = Robot(str)
r.greet()
# ATM
atm = ATM(50000)
print("Balance =", 50000)
n = int(input("Enter the amount to withdraw: "))
print("Remaining balance: ", atm.withdraw(n))
n = int(input("Enter the amount to deposit: "))
print("Updated balance: ", atm.deposit(n))

# Enter your name:john
# Robot says hello to john
# Balance = 50000
# Enter the amount to withdraw: 5000
# Remaining balance:  45000
# Enter the amount to deposit: 200
# Updated balance:  45200