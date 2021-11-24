"""
Make a class called Restaurant. The __init__() method for Restaurant should store two attributes:  a restaurant name and a cuisine type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open. Make an instance called restaurant from your class. and then call both methods.

Note:
if the time is in between 11hrs and 23hrs it should print 
    Restaurant Open
"""

from datetime import datetime


class Restaurant():
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe_restaurant(self):
        print("Welcome to " + self.name + "\n" + self.type)

    def open_restaurant(self):
        now = datetime.now()
        if now.hour >= 11 and now.hour <= 23:
            print("Restaurant Open")
        else:
            print("Restaurant Closed")


p = input("Enter the Restaurant name: ")
d = input("Enter the Dish: ")
r = Restaurant(p, d)
r.describe_restaurant()
r.open_restaurant()


# Enter the Restaurant name: paradise
# Enter the Dish: biryani
# Welcome to paradise
# biryani
# Restaurant Open