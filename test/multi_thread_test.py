# coding=UTF8
# 测试多线程模块threadpool
import threadpool
import random
import time
import datetime

def calculate(nums):
    print nums
    a = random.randint(0, 100)
    b = random.randint(0, 100)
    time.sleep(5)
    print datetime.datetime.now().strftime("%H:%M:%S")


if __name__ == '__main__':
    nums = []
    for i in range(1, 20):
        nums.append(i)

    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(calculate, nums)
    [pool.putRequest(req) for req in requests]
    pool.wait()
