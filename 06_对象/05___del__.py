#   __init__ 相当于构造函数
#   __del__ 相当于析构函数

class Cat:
    def __init__(self, name):
        self.name = name
        print("%s init" % self.name)

    def __del__(self):
        print("%s del" % self.name)


tom = Cat("Tom")

print(tom.name)
# del tom
print("-" * 50)

