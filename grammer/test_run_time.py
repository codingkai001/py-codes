from array import array
from time import time

a = [i for i in range(10000000)]
start = time()
"""测试代码块开始"""
found = 0
for i in range(1000):
    if i in a:
        found += 1
"""测试代码块结束"""
end = time()
print("共用时%.6f秒" % (end - start))
