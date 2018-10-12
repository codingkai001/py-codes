import random
import math
import os
import time

"""from math import *
x = 2 ** 5
# x的y次幂
print(x)
# x除以y的整数部分
x = 10 // 2.3
print(x)
a = 5
b = 8
print(a > b)
print(a < b)
print(2 > 1 > 0)
a = 'hello'
b = "python"
print(a > b)
print(4 > 3 and 3 < 8)
a = 1
if a < 8:
    print("*")
    print('/', "256")
for a in [1, 2, 3, 4, 5, 6]:
    print(a)
a = pow(2, 5)
print(a)
c = pi * e
print(c)
a = "baidu.com", "python"
print(a)
import math
import random

# 数值交换
a = 9
b = 8
a, b = b, a
print(a)
print(b)
# python不需要指定数据类型，内部会根据变量的大小，类型自动转化
a = len(str(2 ** 100000))
print(a)
m = "python"
n = "abc"
print(id(m),  id(n))                         # 用id语句来检查变量指向的是否是同一对象（不等价于相等的值）
# ***********************************字符串（具有不可变性）*****************************
在字符串前面加r或者R指明一个自然字符串，则不会被特殊处理，例如转义字符
s = "random_random"
print(s[0:len(s)])  # x[I:J]    分片：提取出X序列中索引从I开始，直到J（不包括）的部分内容
print(s[:-3])  # s[:] 默认取出s的所有内容     s[:-x]  提取出除最后X个元素外的所有内容
print(s[::x])   #s[::x] 步长为X
c = s + "apple"
print(c)  # '+' 可以将两个字符串合并起来
a = s * 8
print(a)  # '*' 可以将字符串成倍的复制
s = 'A' + s[:3]  # 可以建立新的字符串并取以原来的名称
print(s)
# s[1] = 'A'        TypeError: 'str' object does not support item assignment
# 不能对字符串的某一位置进行赋值而改变字符串
print(s.find('a'))  # 字符串的find方法，返回所查找的子串的初始位置，或者-1（未找到）
print(s.replace("an", "APPLE"), '\n', s)  # 字符串的replace方法，搜索和替换内容，原字符串内容不变
s = "pyth"
s += "on"  # 除了数字，字符串也可以进行增量运算
print(s)
# *****************************************if条件语句*****************************************
print("input a number you'd like:")
num = int(input())
print("the number you input is %d" % num)
if num > 10:  # 条件的语句体必须缩进4个空格
    print("it's too big!")
elif num < 10:
    print("it's too small!")
else:
    print("you are right!")
# ***************************************三元操作符*********************************************
a = 5 if 5 < 3 else 8  # A = Z if X else Y ：如果X为真，则A = Z,否则A = Y
print(a)

x = 32
y = 52
c = x if x < y else y
print(c)
# ******************************************for循环语句*********************************************
Str = "hello!"
for a in range(0, len(Str), 1):  # 等价于range(len(Str))
    print(Str[a])
for i in [1, 2, 3, 4, 5, 6]:  # in +[List内容]或List名称，的到每一个元素的值
    print(i)
# range函数的用法：
#                               这个函数可以创建一个 <数字> 元素组成的列表。即原List的索引组成的LIst
#                               这个函数最常用于for循环（关于for循环，马上就要涉及到了）
#                               函数的参数必须是整数，默认从0开始。返回值是类似[start, start + step, start + 2*step, ...]的列表。
#                               step默认值是1。如果不写，就是按照此值。
#                               如果step是正数，返回list的最最后的值不包含stop值，即start+step这个值小于stop；如果step是负数，start+istep的值大于stop。
#                               step不能等于零，如果等于零，就报错。
# range(start, stop, step)：
#                                start：开始数值，默认为0,也就是如果不写这项，就是认为start=0
#                                stop：结束的数值，必须要写的。
#                                step：变化的步长，默认是1,也就是不写，就是认为步长为1。坚决不能为0
#                                range(9)：只写一个数值，默认为stop的值等于9，等价于range(0,9,1)
#                                step为1的时候只用写stop的值，step不为1的时候需要三个参数全部写出来.eg:range(0,9,2)
allcs = []  # 列出100以内所有的能被三整除的正整数
for n in range(1, 100, 1):
    if not n % 3:
        allcs.append(n)
allcs.reverse()             # 翻转
print(allcs)
a = [1, 2, 3, 4, 5]                 # 将两个数组中对应元素相加：zip(a, b)返回一个元组如[(1, 10), (2, 9), (3, 8)]，长度以较短的数组为准
b = [10, 9, 8, 7, 6, 11]
c = []
for x, y in zip(a, b):
    c.append(x + y)
print(c)
c.clear()          # 清空c数组
for i in range(len(a)):        # 较短的数组
    c.append(a[i] + b[i])
print(c)
# ****************************************while循环语句*********************************************
# 简单猜数字游戏
i = 0
count = 3
while i < 4:
    count = 3 - i
    num = int(input("请输入一个0~9的数字：")) % 10
    result = random.randint(0, 9)
    if num == result:
        print("恭喜你猜对了！正确答案是%d" % result)
        break
    elif count > 0:
        print("很遗憾你猜错了！正确答案是%d,你输入的值是%d,你还有%d次机会" % (result, num, count))
        i += 1
    else:
        print("你都猜错了，游戏结束！")
        break
# **********************
# while...else循环
count = 0
while count < 5:
    print(count, " is  less than 5")
    count += 1
else:
    print(count, " is not less than 5")
# for...else循环
for n in range(99, 1, -1):
    root = math.sqrt(n)
    if int(root) == root:
        print(n)
        break
else:
    print("nothing!")

# ************************************* 文件 * ****************************************************
f = open("C:\\Users\\Coding-Kai\\Desktop\\控制台颜色输出属性.txt", "a+t")           # 打开文件,如果不加说明默认是"r",即只读文件
for n in f:                                                                     # 读取文件内容
    print(n)
f.write("\n人生苦短，我用python")                          # 追加内容
f.close()                                                                       # 关闭文件
# 使用with,可以自动安全地关闭文件
with open("C:\\Users\\Coding-Kai\\Desktop\\控制台颜色输出属性.txt", "r+t") as f:         # 另一种打开方式
    print(f.read())
# read函数读取全部文件内容，还有readline（每次读取一行内容）,
# readlines（返回一个列表，表中每个元素就是文件中的一行内容）
# 文件状态(属性)
file_stat = os.stat("C:\\Users\\Coding-Kai\\Desktop\\控制台颜色输出属性.txt")
print(file_stat)                # 打印 file_stat.+某一属性 可以查看该文件某的一属性
print(time.localtime())
# seek函数以字节为单移动文件指针
f = open("C:\\Users\\Coding-Kai\\Desktop\\控制台颜色输出属性.txt", "a+t")
f.seek(0)           # 将指针移动到文件首
print(f.tell())     # 打印当前指针的位置（距文件首的字节数）
# ******************************************格式化输出**************************************************************
s = "duck"
age = 25
print("{0}  is  {1} years old !".format(s, age))  # format方法用参变量的值代替格式符，格式符必须一一对应
print("why is {0}  here?".format(s))
print('{0:.3}'.format(1 / 6))  # 格式符:.3    参变量的值保留小数点后三位
print('{0:_^11}'.format('hello'))  # 格式符:填充字符^宽度，用该字符填充字符串，且宽度为width
a = 52.3654
b = 250
s = "hello"
print("%-8.3f is float,%6d is int, %10s is string" % (a, b, s))    # 与C语言的格式化输出一致
# *******************************************数据结构****************************************
# python中有四种内建的数据结构-----列表，元组，字典与集合,其中列表、元组和字符串都有切片操作
# @列表是处理一组有序项目的数据结构，相当于数组（数字数组+字符数组）
# shopping list
# !/usr/bin/python
# Filename:using_list.py
shop_list = ['apple', 'mango', 'carrot', 'banana']
print("I have", len(shop_list), ' items to purchase')
print('These items are', end=':')
for item in shop_list:
    print(item, end=',')
print("I also have to buy rice")
shop_list.append('rice')
print("My shopping list is now :", shop_list)
print('I will sort my list')
shop_list.sort()        # 排序
print('Sorted shopping list is now', shop_list)
print('I will buy the ', shop_list[0])
old_item = shop_list[0]
del shop_list[0]        # del 删除列表中的项目
print('I bought the', old_item)
print('My shop list is now', shop_list)
print(shop_list.__sizeof__())
# @元组用来将更多的对象集合在一起，与列表很相似，但是和字符串一样是不可变的，元组通常用在使语句或函数能够安全的采用一组值的时候，即被使用的元组的值不会改变
# !/usr/bin/python
# Filename:using_tuple.py
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is ', len(zoo))
new_zoo = ('monkey', 'camel', zoo)      # 元组之内的元组仍旧会保持其特性
print('Numbers of cages in the new zoo is ', len(new_zoo))
print('All animals in the new zoo are: ', new_zoo)
print('Animals brought from old zoo are :', new_zoo[2])
print("Last animal brought from old zoo is ", new_zoo[2][2])
print('Numbers of animals in the new zoo is ', len(new_zoo)-1+len(new_zoo[2]))
# @字典类似于通过联系人姓名查找地址的地址簿，即把键（姓名）和值（地址）联系在一起，并且键必须是唯一的，
# 只能使用不可变的对象，例如字符串作为字典的键，但是值可以是随意的
# dict = {key1:val1, key2:val2, key3:val3}，字典中的键/值是没有顺序的，使用前要自己排序
# !/usr/bin/python
# Filename:using_dict.py
ab = {'lucy': 'lucy@lucy.com', 'alex': 'alex@alex.com',
    'fk': 'fk@fk.com', 'fb': 'fb@fb.com'}   # ab is short for 'a'ddress 'b'ook
print('lucy`s address is ', ab['lucy'])
del ab['fb']    # 删除'fb'的键值部分
print('\nThere are %d contacts in the book' % len(ab))
for name, address in ab.items():    # 用item方法来使用每一个键/值对,返回一个元组，每一个元素都是键/值对
    print('{0}’s address is {1} '.format(name, address))
ab['fx'] = 'fx@fx.com'  # 增加键值部分
if 'fx' in ab:  # 检验键/值对是否存在
    print('\nfx’s address is', ab['fx'])
# @集合石没有顺序的简单对象的聚集，当对象的存在比顺序或者出现的次数重要时用集合，集合有交、并、补等运算，与数学中一致
bri = set(['a', 'b', 'c', 'd'])
bric = bri.copy()
bric.add('e')
print('a' in bri)   # 检验元素是否在集合内
print(bric & bri)   # 交集
print(bric.issuperset(bri))  # 超集      """
# *****************************************************面向对象编程*****************************************************
"""
class Person:   # 类名首字母大写
    pass    # 空类体
p = Person()
print(p)


class Person:
    def say_hi(self):   # 类的方法，默认第一个参数为self
        print('Hello! How are you?')
p = Person()
p.say_hi()
# _init_方法在类的对象被建立时 ，马上运行。这个方法可以对对象做一些初始化，相当于C++，JAVA，C#中的构造函数


class Person:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print('Hi! My name is', self.name)
p = Person('fengkai')   # 把参数跟在类名后面传递给_init_方法
p.say_hi()
'''
类和对象变量：只在类和对象的前提下有效
有两种类型的域——类的变量和对象的变量，它们是根据谁拥有这些变量而区分的
类的变量由类的所有对象共享使用，当某个对象对变量改动时，也会在其他对象上有改动
对象的变量由每个对象（实例）拥有，不是共享的，不同对象的变量名称可以相同，它们不在同一个域，并不相互关联
'''


class Robot:
    population = 0  # 类变量
# 同名的对象变量会隐藏类变量

    def __init__(self, name):  # name是对象变量，用self为其赋值
        self.name = name    # 用对象.对象变量来引用对象变量
        print('Initialize {0}'.format(self.name))
        Robot.population += 1   # 用类名.类变量来引用类变量

    def __del__(self):
        print('{0} is being destroyed!'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one'.format(self.name))
        else:
            print('There were still {0:d} Robots working'.format(Robot.population))

    def say_hi(self):
        print('Greeting, My master call me {0}'.format(self.name))

    def how_many():
        print('We have {0:d} Robots'.format(Robot.population))

    how_many = staticmethod(how_many)   # 静态类方法


droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('\nRobots can do some works here.\n')
print('Robots have finished their works,let`s destroy them')

del droid1  # 调用_del_方法，删除对象
del droid2

Robot.how_many()        """


# 继承


class SchoolMember:  # 基本类（父类）
    """Represent any school member"""

    def __init__(self, name, age):  # 初始化对象的基本部分
        self.name = name
        self.age = age
        print('Initialize School Member: {0}'.format(self.name))

    def tell(self):
        """Tell my details"""
        print('Name:{0} Age:{1}'.format(self.name, self.age), end='  ')


class Teacher(SchoolMember):  # 把基本类（父类）跟在子类的后面作为一个元组，即该子类继承了父类
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)  # 方法的继承
        self.salary = salary
        print('Initialize Teacher:{0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Salary:{0:d}'.format(self.salary))


class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('Initialize Student:{0}'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks:{0:d}'.format(self.marks))


t = Teacher('Mrs liu', 25, 3500)  # 调用_init_方法，并且将基本参数传递给它
s = Student('Lucy', 18, 95)

print()
members = [t, s]  # 对象列表
for member in members:
    member.tell()
