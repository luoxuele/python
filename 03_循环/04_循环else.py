# 如果循环中是break终止循环，则不执行else语句

for i in range(5):
    print(i)
    # break
    continue
else:
    print("for else")

i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("while else")