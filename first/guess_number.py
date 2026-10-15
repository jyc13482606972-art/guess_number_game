
import random

answer = random.randint(1, 100)
count = 0

print("欢迎来到猜数字小游戏！")
print("我已经想好了一个 1 到 100 之间的数字。")

while True:
    guess = int(input("请输入你猜的数字："))
    count += 1

    if guess > answer:
        print("大了！")
    elif guess < answer:
        print("小了！")
    else:
        print(f"恭喜你，猜对了！答案是 {answer}")
        print(f"你一共猜了 {count} 次。")
        break
