"""
计算两个日期间隔的天数
"""
import time
from math import fabs

__Author__ = "冯凯"
__Date__ = 20170723

date1 = str(input("请输入第一个日期（例如：20170702）："))
date2 = str(input("请输入第一个日期（例如：20170702）："))
tup1 = time.strptime(date1, "%Y%m%d")
tup2 = time.strptime(date2, "%Y%m%d")
sec1 = time.mktime(tup1)
sec2 = time.mktime(tup2)
days = fabs(sec1 - sec2) / 3600 / 24
print("日期间隔天数为：%d" % days)
