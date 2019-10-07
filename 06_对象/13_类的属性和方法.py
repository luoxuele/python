# 1. 类的方法和属性都可以通过类名和实例对象调用
# 2.  实例对象的属性优先类属性

class Person(object):
    num = 100
    country = "中国"
    __hello = "哈喽"

    @classmethod
    def get_hello(cls):
        return cls.__hello

    @classmethod
    def set_hello(cls, new_hello):
        cls.__hello = new_hello

    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("小明", 22)
p2 = Person("小红", 20)

print(p2.country)
print(p1.country)
print(Person.country)

# p2.country = "美国"
Person.country = "美国"
print(p2.country)
print(p1.country)
print(Person.country)

# 读时共享，写时复制？
# 实例对象的变量优先类变量？

print(id(Person.num))
print(id(p2.num))

# def xxx(self):
#     return "xxxx"
# Person.get_hello = xxx


def xxx(new_hello, self = Person):
    print(self)
    self._Person__hello = new_hello

xxx("haha")

print(p1.get_hello())
print(Person.get_hello())