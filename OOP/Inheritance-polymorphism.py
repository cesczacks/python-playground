# Inheritance
class Animal(object):
    def run(self):
        print("Animal is running")

class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')

class Cat(Animal):
    def run(self):
        print('Cat is running...')

class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()


print(isinstance(cat, Animal))

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())
run_twice(Tortoise())








