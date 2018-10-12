import string
import random
import time

"""
# 输出指定范围内的不足数，完全数和丰沛数
list_less = []
list_perfect = []
list_more = []
raw_input = int(input("please input a max number :"))
for i in range(2, raw_input):
    Sum = 0
    for j in range(1, i):  # 计算因子之和
        if i % j == 0:
            Sum += j
    if Sum == i:
        list_perfect.append(i)
    elif Sum < i:
        list_less.append(i)
    else:
        list_more.append(i)
print("不足数：", list_less)
print("完全数：", list_perfect)
print("丰沛数：", list_more)
"""

"""


# 希尔排序
def shell_sort(lists):
    gap = len(lists) // 2
    while gap > 0:
        for i in range(gap, len(lists)):
            j = i - gap
            while j >= 0 and lists[j] > lists[j + gap]:  # swap
                lists[j], lists[j + gap] = lists[j + gap], lists[j]
                j -= gap
        gap //= 2
    return list


# 主函数
Max = int(input("请输入要排序的元素个数："))
array = [random.randint(0, 100000) for i in range(0, Max)]
shell_sort(array)
for m in array:
    print(m, end='_', )  # end=' ',可以控制在一行输出"""
"""
# 函数调用函数
def func1(str1):
    resultStr = ' '
    for char in str1:
        if char in string.digits:
            resultStr = resultStr + char
            if resultStr:
                return resultStr
            else:
                return -1
def func2(str1):
    if len(str1) > 0:
        str1 = str1.strip()     # strip方法返回字符串头尾去除指定字符的字符串，默认为空格
        resultInt = func1(str1)
    else:
        resultInt = 0
    return resultInt
# main program
responseStr = input("please input a string:")
print(func2(responseStr))

# 用递归求数列1/3+2/5+3/7+4/9+·····的和，输入一个正整数n，输出前n项的和，保留15位小数


def func(n):
    if n == 0:
        return 0
    else:
        return n/(2*n+1) + func(n-1)
temp = int(input("请输入数列的项数："))
print("the sum is %.15f" % func(temp))
# n!


def func(n):
    if n == 1:
        return 1
    else:
        return n * func(n-1)
temp = int(input("请输入最大值："))
for i in range(1, temp+1):
    print("%d! = %-d" % (i, func(i)), "    length is ", len(str(func(i))))
with open("C:\\Users\\Coding-Kai\\Desktop\\test.txt") as f:
    print(f.read(), end=' ')
print(f.name, f.closed)


# bubble_sort


def bubble_sort(array):
    for i in range(0, len(array)):
        for j in range(1, len(array) - i):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]


num = int(input("请输入要排序的元素个数："))
n = [random.randint(0, 10000) for i in range(0, num)]
bubble_sort(n)
print(n)


# shell_sort


def shell_sort(lists):
    gap = len(lists) // 2
    while gap > 0:
        for i in range(gap, len(lists)):
            j = i - gap
            while j >= 0 and lists[j] > lists[j + gap]:
                lists[j], lists[j + gap] = lists[j + gap], lists[j]
                j -= gap
        gap //= 2


num = int(input("请输入要排序元素的个数："))
List = [random.randint(0, 10000) for i in range(0, num)]
shell_sort(List)
for i in List:
    print("%-4d" % i, end='   ')            """


# n!_ver2.0


class N:
    def func(self, n):
        f = 1
        f *= n
        return f


func = staticmethod(func)

num = int(input("请输入要计算阶乘的最大值："))
for i in range(1, num + 1):
    print('n!=%d' % N.func(i))
