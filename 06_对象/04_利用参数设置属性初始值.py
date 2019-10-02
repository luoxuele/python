class Cat:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("%s eat fish" % self.name)


tom = Cat("汤姆")
tom.eat()
print(tom.name)

