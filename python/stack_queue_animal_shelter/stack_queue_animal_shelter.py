from stack_and_queue.stack_and_queue import Queue

class Cat:
    def __init__(self,name):
        self.name= name
    def __str__(self) -> str:
        return f"Cat with name {self.name}"

class Dog:
    def __init__(self,name):
        self.name= name
    def __str__(self) -> str:
        return f"dog with name {self.name}"

class Shelter :
    def __init__(self):
        self.cats = Queue()
        self.Dogs = Queue()
    def enqueue(self,animal):
        if str(animal) == str(Cat(animal.name)):
            self.cats.enqueue(animal)
        elif animal ==Dog(animal.name):
            self.dogs.enqueue(animal)
    def dequeue(self,pref):
        if pref == "cat":
            return self.cats.dequeue()
        elif pref == "dog":
            return self.dogs.dequeue()
        else:
            return "null"
