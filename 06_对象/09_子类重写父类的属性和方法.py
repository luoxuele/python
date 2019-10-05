# 重写，实际上就是把父类的属性和方法覆盖掉
# 重写的东西自然不会用继承的了

# 自定义师傅类
# Master 是object的子类 object是Master的父类(相对)
class Master(object):
    # 构造方法
    def __init__(self):
        print("Master")
        # 属性
        self.kongfu = "古法"

    # 会制作煎饼果子
    def make_cake(self):
        print("古法煎饼果子")

    def dayandai(self):
        print("大眼袋")

# 自定义新东方
class School(object):
    # 构造方法
    def __init__(self):
        print("School")
        # 属性
        self.kongfu = "现代"

    # 会制作煎饼果子
    def make_cake(self):
        print("现代煎饼果子" )

    def xiaoyandai(self):
        print("小烟袋")


# 自定义徒弟类
# 大猫
# 猫氏煎饼果子配方
# 会制作猫氏煎饼果子
class Prentice(Master, School):

    # 构造方法
    # 重写: 子类继承了父类 子类实现了父类的方法 做自己特有的事情
    def __init__(self):
        print("Prentice")
        self.kongfu = "猫氏"

    # 会制作煎饼果子
    def make_cake(self):
        print("猫氏煎饼果子")


damao = Prentice()
damao.make_cake()
damao.dayandai()
damao.xiaoyandai()