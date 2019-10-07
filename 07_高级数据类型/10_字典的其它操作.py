xiaoming = {"name": "小明",
            "age": 18}

# 1. 统计键值对数量
print(len(xiaoming))

# 2. 合并字典
temp_dict = {"height": 1.75,
             "age": 20}

# 合并的字典存在相同的key，会覆盖原来的值
xiaoming.update(temp_dict)
print(xiaoming)

# 3. 清空字典
xiaoming.clear()
print(xiaoming)
