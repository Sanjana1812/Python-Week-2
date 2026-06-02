class Animal:

    def sound(self):
        print("Animal Sound")


class Dog(Animal):

    def sound(self):
        print("Dog says Bark")


class Cat(Animal):

    def sound(self):
        print("Cat says Meow")


# Creating objects
dog = Dog()
cat = Cat()

# Calling methods
dog.sound()
cat.sound()
