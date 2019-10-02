class Cat:
    def __init__(self, name):
        self.name = name
        print("%s init" % self.name)

    def __del__(self):
        print("%s del" % self.name)

    def __str__(self):
        return "Cat <name: %s>" % self.name

tom = Cat("汤姆")
print(tom)