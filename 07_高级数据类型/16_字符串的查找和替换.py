hello_str = "hello world"

print(hello_str.startswith("hello"))
print(hello_str.endswith("world"))

print(hello_str.find("llo"))
print(hello_str.find("abc"))
# find 不存在则返回-1， index不存在则报错


# 返回的是一个新的字符串，原有的字符串不会改变
print(hello_str.replace("world", "python"))
print(hello_str)