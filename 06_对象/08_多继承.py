class Master(object):
    def __init__(self):
        print("Master")
        self.kongfu = "古法煎饼果子配方"

    def make_cake(self):
        print("按照《%s》制作煎饼果子" % self.kongfu)

    def dayandai(self):
        print("大烟袋")


class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代煎饼果子配方"

    # 会制作煎饼果子
    def make_cake(self):
        print("按照<%s>制作煎饼果子" % self.kongfu)

    # 香烟
    def xiaoyandai(self):
        print("小烟袋")

class Prentice(Master, School):
    pass

# 继承多个父类时，会继承第一个父类的所有属性和方法，后面的父类如果有不同名的属性和方法
# 也会继承，同名的不管了
tudi = Prentice()
print(tudi.kongfu)
tudi.make_cake()
tudi.dayandai()
tudi.xiaoyandai()

