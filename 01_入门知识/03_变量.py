'''
python中变量定义的特点
1. 动态类型，根据赋值自动确定变量的类型
2. 多变量同时赋值，元组xxx?


'''

num1 = 4
print(type(num1))

num1 = "hello world"
print(type(num1))

num2 = 4
# print(num1 + num2)  # TypeError: can only concatenate str (not "int") to str


var1, var2 = "hello", 123
var1, var2 = var2, var1  # 变量交换
print(var1)
print(var2)



