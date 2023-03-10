class  Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog(Animal):
    def bark(self):
        print("The dog barks")
class Cat(Animal):
    def meow(self):
        print("The cat meows")
class Horse(Dog,Cat):
    def gallop(self):
        print("The horse gallops")
d=Dog()
d.bark()
d.legs()
d.fur()
c=Cat()
c.meow()
c.legs()
c.fur()
h=Horse()
h.gallop()
h.bark()
h.meow()