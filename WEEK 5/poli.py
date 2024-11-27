class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"


# Polymorphism in action
for animal in [Dog(), Cat()]:
    try:
        print(animal.speak())
    except AttributeError as e:
        print("Ooops, we have an error", e)
