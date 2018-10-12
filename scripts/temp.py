"""
输入三个整数x,y,z，请把这三个数由小到大输出
"""
import string


def main():
    for i in range(1, 8, 2):
        print(' ' * int(4 - (i + 1) / 2) + '*' * i)
    for i in range(5, 0, -2):
        print(' ' * int(4 - (i + 1) / 2) + '*' * i)


if __name__ == "__main__":
    main()