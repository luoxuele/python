# 1. 判断空白字符串
space_str = "    \t\n\r"

print(space_str.isspace())


# 2. 判断字符串中是否包含数字
# num_str = "1.1" # 都不能判断小树
num_str = "\u00b2"
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal())
print(num_str.isdigit())
print(num_str.isnumeric())