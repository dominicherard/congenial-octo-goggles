# verysimple.py
# This will be the basis for a simple trial Github project.

from random import choice

from conversator import Conversator

class MyType:
    def __init__(self):
        self.greeting1 = "Howdy"
        self.greeting2 = "Hey"
        self.greeting3 = "Cheers"
        self.greetings = [self.greeting1, self.greeting2, self.greeting3]

    def greet(self, name):
        return choice(self.greetings) + " " + name + "!"

print("Hello World!")
print("I enjoy working with", end = " " )
print("groovy people!")

duder = MyType()
cleverconversator = Conversator("phat")
print(duder.greet("Dominic"))
print(duder.greet("Matt"))
print(duder.greet("Nidal"))
print("I prefer {} rhymes!".format(cleverconversator.dropwordoftheday()))