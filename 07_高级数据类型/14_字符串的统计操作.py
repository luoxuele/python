hello_str = "hello hello world"

# 1. 统计字符串长度
print(len(hello_str))

# 2 统计子串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("abc"))

# 3. 某个子串出现的索引
print(hello_str.index("llo"))
# print(hello_str.index("abc")) 找不到子串，则报错