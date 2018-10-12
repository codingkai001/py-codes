from wxpy import *
from time import sleep

bot = Bot()

if __name__ == '__main__':
    my_friend = bot.friends().search(keywords='陈宇')
    while True:
        if len(my_friend):
            my_friend[0].send('Hello WeChat!')
            sleep(10)
        else:
            print("没找到好友")
            break
