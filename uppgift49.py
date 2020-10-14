# Förståelse kring objektorientering genom djur och deras läten, egenskaper
import random


class Dog:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Woff!")

    def make_trick(self):
        tricks = ['roll', 'sit', 'jump']
        print(f"{self.name}: making trick {random.choice(tricks)}")


class Cat:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name}: Mjau!")

    def make_trick(self):
        print(f"{self.name}: Cat's don't make tricks on demand!")



class Parrot:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        speak = input(f"Say something to {self.name}! ")
        print(f"***{self.name} making trick mimic***")
        print(f"{self.name}: {speak}")


