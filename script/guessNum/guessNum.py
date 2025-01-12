import random

def guess_game():
    # 生成一个 1 到 100 之间的随机数
    num = random.randint(1, 100)
    # 记录猜测次数
    guess_times = 0
    while True:
        guess_times += 1
        guess = int(input("请输入你的猜测："))
        if guess == num:
            print("恭喜你，猜对了！你一共猜了%d 次。" % guess_times)
            break
        elif guess > num:
            print("你猜的数字大了，请重新输入。")
        else:
            print("你猜的数字小了，请重新输入。")
if __name__ == "__main__":
    guess_game()
    input("游戏结束，按回车键退出...")