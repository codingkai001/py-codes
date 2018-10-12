# !/usr/bin/python
# Filename:Guess2.0.py

# 猜数字游戏：用户有5次机会根据提示不断输入值，直到与系统产生的随机数相同即可获胜
import random

result = random.randint(0, 100)
raw_input = int(input("请输入一个0~100间的数字："))
i = 1
while i < 5:
    if raw_input > result:
        print("太大了！你还有%d次机会，请重新输入：" % (5 - i))
    elif raw_input < result:
        print("太小了！你还有%d次机会，请重新输入：" % (5 - i))
    else:
        print("恭喜你猜对了！")
        break
    i += 1
    raw_input = int(input())
if i == 5 and raw_input != result:
    print("很遗憾，你没有猜对！")
    print("正确答案是%d" % result)
if i == 5 and raw_input == result:
    print("恭喜你猜对了！")
