def my_func(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # print(kwargs["name"])
    # print(kwargs["age"])


my_func(name="田玲利", age=23)

print("-----")
my_func()