from functools import reduce
from time import time
from random import randint
from operator import add
from array import array

a = (randint(1, 10000) for i in range(1000000000))
arr = array('d', a)
start = time()
"""测试代码块开始"""
reduce(add, a)
"""测试代码块结束"""
end = time()
print("共用时%.6f秒" % (end - start))
