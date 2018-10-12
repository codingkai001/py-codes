from multiprocessing import Pool, Process
import os
import time
import random


def long_process(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.randint(2, 10))
    end = time.time()
    print('Task %s runs %.2f s.' % (name, (end - start)))


if __name__ == '__main__':
    start = time.time()
    print('Parent Process %s start...' % os.getpid())
    p = Pool(4)  # 进程池对象， arg=同时运行的进程数，为cpu核心数
    for i in range(8):
        p.apply_async(long_process, args=(i + 1,))
    print('Waiting for all subprocesses done...')
    p.close()  # 多进程调用结束，不再添加进程
    p.join()  # 等待所有子进程运行完毕
    end = time.time()
    print('All subprocesses done with %.2f s' % (end - start))
