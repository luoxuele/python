# str   int float   repr    eval

str1 = "1000"
num = int(str1, 2)
# 把str1 按2进制转换成10进制的数字，数字默认是10进制的

print(type(num))
print(num)

str2 = "3.14"
num = float(str2)
print(type(num))
print(num)

ll = [1,2,3,4]
str1 = str(ll)
print(type(str1))
print(str1[1:-1])

# repr(x )	将对象 x 转换为表达式字符串 这个字符串是给python看的
num2 = 3.14
mystr2 = repr(num2)
print(type(num2))
print(type(mystr2))

# eval(str )	用来计算在字符串中的有效Python表达式,并返回一个对象
num1 = eval(input("请输入一个表达式"))
print(num1)