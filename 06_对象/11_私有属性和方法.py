# python中的私有属性是假的
# 私有属性应有的特点：
#     1. 只能在本类中访问
#     2. 子类继承，私有变量应该不能访问（继承） # 实际上全都继承了
#
# 但python中用双下划线定义的私有方法和属性，解释器自动在这个变量名加了(_类名)
# 实现了表面上的私有，但实际上还是可以访问的，解释器并没有加以显示


class Master(object):

    def __init__(self):
        self.kongfu = "古法"
        self.__money = 1000000

    def make_cake(self):
        print("制作古法煎饼果子")
        print(self.__money)
        self.__hello_python()

    def __hello_python(self):
        print("你好 python")


lishifu = Master()
# lishifu.make_cake()

# lishifu.__hello_python()
# print(lishifu.__money)

print(lishifu._Master__money)
lishifu._Master__hello_python()


class Prentice(Master):

    def xx(self):
        print("xxx")


damao = Prentice()
print(damao.kongfu)
print(damao._Master__money)
damao._Master__hello_python()
