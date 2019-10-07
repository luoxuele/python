xiaoming = {"name": "小明"}

# 1. 取值
print(xiaoming["name"])
# print(xiaoming["name1"]) # 不存在会报错

# 2. 增加，修改
xiaoming["age"] = 18    # key不存在则添加
xiaoming["name"] = "小小明"    # key存在，则修改
print(xiaoming)

# 3. 删除
xiaoming.pop("name")
print(xiaoming)
# xiaoming.pop("name111")     #不存在key则报错