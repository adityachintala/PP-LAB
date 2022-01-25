# Make a class called Restaurant. The init () method for Restaurant should store two attributes: a restaurant_name
# and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a
# method called open_restaurant() that prints a message indicating that the restaurant is open. Create three
# different instances from the class, print the two attributes individually, and then call both methods for
# each instance.

from datetime import datetime


class Restaurant:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def describe(self):
        print("Restaurant name :", self.name)
        print("Cuisine type :", self.type)

    def open(self):
        time = datetime.now()
        hr = int(time.strftime('%H'))
        if (hr >= 11 and hr <= 23):
            print("Open")
        else:
            print("Closed")


r1 = Restaurant("Pizza Hut", "Pizza")
r1.describe()
r1.open()
r2 = Restaurant("McDonalds", "Fast Food")
r2.describe()
r2.open()