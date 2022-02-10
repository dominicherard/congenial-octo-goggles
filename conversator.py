# conversator.py

from random import choice

class Conversator:
    def __init__(self, wordoftheday):
        self.wordoftheday = wordoftheday
        self.starterlines = [
            "Boy, hasn't the cold been brutal this winter!",
            "I can't believe you got your products shipped so early!",
            "Let me tell you. I know this guy. He's amazing!",
            "It's so cold. You gotta try this brand of lotion!",
            "Typically, I can't stand IPA beer, but this one is phenomenal!"
        ]
    def conversate(self):
        return choice(self.starterlines)

    def dropwordoftheday(self):
        return self.wordoftheday

# communicator = Conversator("dope")
# print(communicator.conversate())
# print("I hope your day is {}!".format(communicator.dropwordoftheday()))