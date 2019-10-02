class Cat:
    def eat(self):
        print("小猫爱吃鱼")

    def drink(self):
        print("小猫要喝水")

    def say(self):
        print(self.name)


tom = Cat()
tom.eat()
# tom.name = "汤姆"

tom.say()
