from array import array
from random import random
from timeit import timeit


def write_double():
    # 在array中存入10000000个double数
    floats = array('d', (random() for i in range(10 ** 7)))
    fp = open('floats.bin', 'wb')
    # 将array中的数据存入二进制文件中
    floats.tofile(fp)
    fp.close()


def read_double():
    floats = array('d')
    fp = open('floats.bin', 'rb')
    floats.fromfile(fp, 10 ** 7)
    fp.close()


if __name__ == '__main__':
    time1 = timeit('write_double()', setup='from __main__ import write_double', number=1)
    time2 = timeit('read_double()', setup='from __main__ import read_double', number=1)

    print('写入用时：' + str(time1))
    print('读取用时：' + str(time2))
