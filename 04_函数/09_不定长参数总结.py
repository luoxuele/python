# def func1(name, no, age=22,xxx):
#     print(age)


#默认参数后面必须也是默认参数，（元组和字典除外）


# 不定长参数元组和默认参数是平级的，位置可以互换
# 不定长参数之字典 必须在函数的尾部

# def my_func(a, b, c=10, *args, **kwargs):
def my_func(a, b, c=10, *args, **kwargs ):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

my_func(1,2,11,222,444, name="小明",age=25)
