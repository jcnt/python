class Pet: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")


class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self): 
        print("Meow")

class Dog(Pet):
    def speak(self): 
        print("Bark")


p = Pet("Tim", 19)
c = Cat("Bill", 17, "black")
d = Dog("Jill", 13)

p.show()
c.show()
d.show()
p.speak()
c.speak()
d.speak()
