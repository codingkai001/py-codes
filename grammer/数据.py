import pickle

"""
# 进制表示
a = 0o123               # 前缀0o表示八进制（Python 3.x）
b = 0x125              # 前缀0x表示十六进制
c = 0b10101          # 前缀0b表示二进制
d = 121                  # 十进制
s = 2 + 3j              # a + bj(大写或小写)表示一个复数
# Python关系运算符链与数学运算相同，与大多数编程语言不同
f = 5
print(0 <= f <= 10)             # True，0 <= 5and 5 <= 10
print(0 <= f <= 2)               # False，0 <= 5 and 5<= 2
# 多重赋值
A, B, C = 1, 2, 3               # 等价于A = 1，B = 2，C = 3
# 交换变量的值
A, B = B, A                      # 等价于 T = A, A = B, B = A
# 字符串函数
str1 = "*********         123 _hello_ 123_hello               "
result1 = str1.isidentifier()  # 是否为标示符，返回bool
result2 = str1.isdecimal()  # 是否为十进制整数，返回bool
result3 = str1.islower()  # 是否为小写字母，返回bool
result4 = str1.isalnum()  # 是否为数字或字母，返回bool
result5 = str1.center(13, '@')  # arg1=宽度，arg2=填充字符，将字符串置于中间位置，两侧用参数字符填充，宽度小于len时，默认为len，多余的宽度用字符填充在两侧
result6 = str1.count('*', 0, len(str1))  # 返回参数字符在字符串中的个数，后两个参数不加时默认为扫描全部内容，未找到时返回0
result7 = str1.find('@', 0, len(str1))  # 查找指定字符，返回参数字符在字符串中的索引号，未找到时返回-1
# result8 = str1.index('@')   # 返回参数字符在字符串中的索引号,没找到时报错
result9 = str1.isnumeric()
result10 = str1.isdigit()
result11 = str1.isprintable()   # 是否全部为可打印字符，返回bool
result12 = str1.isspace()   # 是否为空白字符和转义字符，返回bool
result13 = str1.istitle()
result14 = str1.join('*jfkjej') # 将参数字符加到字符串首，多个字符时挨个加到首部，字符串长度加倍
result15 = str1.replace('_', '^',-1)   # 将旧的字符替换为新的字符，默认（-1）全部替换，返回新的字符串+旧的字符串
result16 = str1.strip('*')  # strip方法返回字符串头尾去除指定字符的字符串，默认为空格,若没有该字符则返回原字符串
result17 = str1.encode("ascii")     # 严格使用ASCII编码的字节流
print(result16, '\n', str1)
# 操作符和表达式
a, b = 2 << 2, 3 >> 5   # 位运算左移，右移
c, d, e, f = 3 & 5, 3 | 5, 3 ^ 5, ~1   # 位运算AND，OR，XOR，~x==-(x+1)
a = 5 > 3
print(a)
# 全局变量
x = 50


def func_global():
    global x
    print("x is %d" % x)
    x = 20
    print("now x is %d" % x)
func_global()
print("x is %d" % x)


# 非局部变量


def func_outer():
    x = 2
    print("x is %d" % x)

    def func_inner():
        nonlocal x
        x = 5
    func_inner()
    print("changed x to %d" % x)
func_outer()

# 默认参数值


def func(a, b=1, c=5):               # 只有参数列表中最后那些参数可以有默认参数值，在调用参数时没有对应的实参时取默认值。
    print(a*b*c)
func("python")                  # 但是def func(a=1, b)是错的
func("I use python ", c=3)      # 可以使用名字而不按照顺序为参数赋值


def reverse(text):  # 字符串翻转
    return text[::-1]


while True:
    s = input('请输入一个字符串：\n')
    if reverse(s) == s:
        print('这是个回文串')
    else:
        print('这不是回文串')

shoplist = ['apple', 'mango', 'banana']
f = open("C:\\Users\Coding-Kai\Desktop\test.txt", "wt")
pickle._dump(str(shoplist), f)
f.close()
del shoplist
f = open("C:\\Users\Coding-Kai\Desktop\test.txt", "rt")
print(pickle._load(f), end='')
f.close()

# ****************内建函数*************************
# eval将字符串转换为Python表达式
print(eval('12*50'))
# int,float,max,min
print(int('12'))
# *****************************************************     """
round(number=2.365, ndigits=2)  # 该函数返回第一个参数的四舍五入值，保留第二个参数指定的小数，
round(2.36)  # 没有第二个参数时，返回该数最接近的偶数
print(2e4)  # 科学计数法 eg:20000
