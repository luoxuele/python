name_list = ["张三", "李四", "王五", "王小二", "张三"]

print("列表的长度为：%d" % len(name_list))
print("%s 出现了%d次" % (name_list[0], name_list.count(name_list[0])))
name_list.remove("张三")
print(name_list)