# 列表的本质实际上是基于数组的  顺序表

name_list = ["zhangsan", "lisi", "wangwu"]

# 索引
print(name_list[2], name_list[-1])

# 修改
name_list[1] = "李四"

#追加
name_list.append("王小二")

#insert 插入
name_list.insert(1,"小妹妹")

# extend 扩展 有点像合并两个列表
temp_list = ["孙悟空", "猪二哥", "沙师弟"]
name_list.extend(temp_list)

# 删除 remove
name_list.remove("wangwu")

# pop 弹出末尾元素
name_list.pop()

# clear 清空列表
name_list.clear()

print(name_list)

