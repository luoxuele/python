class Animal(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("动物吃东西")


class Dog(Animal):

    def eat(self):
        print("狗吃骨头")

class Cat(Animal):

    def eat(self):
        print("猫吃鱼")


class Person(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("人啥都吃")


wangcai = Dog("旺财", 4)
xiaoming = Person("小明", 22)


def print_info(object):
    print(object.name, object.age)
    object.eat()


print_info(wangcai)
print_info(xiaoming)

# c++多态的3个条件  1、要有继承 2、要有虚函数重写 3、用父类指针（父类引用）
# python中的对象是基于哈希表，所以只要对象的函数名一样就行，其它的都不需要
