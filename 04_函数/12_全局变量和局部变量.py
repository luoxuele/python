a = 3

def func1():
    global a
    a = 4
    print(a)


func1()
print(a)

# 定义了一个和全局变量名相同的局部变量
#     # 关于函数内部使用变量的规则
#     # 当使用函数内部的变量 python会在函数内部先找这个变量(局部变量) 如果找到直接使用
#     # 如果在函数内部没找到 就会到函数外边找变量(全局变量) 直接使用
#     # 如果在函数外部也没有找到 就会报错