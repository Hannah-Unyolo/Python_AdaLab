class Animal:
    def move(self):
        pass
    def make_sound(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flying")

    def make_sound(self):
        print("Chirp")

class Cat(Animal):
    def move(self):
        print("Running")

    def make_sound(self):
        print("Meow")

class Fish(Animal):
    def move(self):
        print("Swimming")

    def make_sound(self):
        print("Bop")