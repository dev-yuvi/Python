class Animal():
    def walke(self):
        print("Walking....")
    def eat(self):
        print("Eating....")
    def run(self):
        print("Running....")

class Dog(Animal):
    def bark(self):
        print("Barking.....")
    

class Cat(Animal):
    def meow(self):
        print("Meow....")


dog=Animal()       
dog.run()

cat=Cat()
cat.meow()