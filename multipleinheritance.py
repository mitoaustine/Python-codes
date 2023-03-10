class  Animal:
    def legs(self):
        print("I have four legs")
    def fur(self):
        print("My body is covered with fur")
class Dog:
    def bark(self):
        print("The dog barks")
class Cat(Animal,Dog):
    def meow(self):
        print("The cat meows")
c=Cat()
c.meow()
c.legs()
c.fur()
c.bark()