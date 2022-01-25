# Write the following classes with class variables, instance variable and illustration the self variable
# i) Robot (to greet the world)
# ii) ATM (to deposit and withdraw amount from ATM machine)


# class Robot
class Robot:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, I am " + self.name)


name = input("Enter name :")
r = Robot(name)
r.greet()


# class ATM
class ATM:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited amount :", amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdrawn amount : ", amount)


balance = int(input("Enter balance : "))
a = ATM(balance)
a.deposit(int(input("Enter amount to deposit : ")))
a.withdraw(int(input("Enter amount to withdraw : ")))
print("Balance :", a.balance)