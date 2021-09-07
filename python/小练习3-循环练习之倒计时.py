"""倒计时工具，同时嵌套对应的星号打印，不嵌套时间计数更精准"""
import time

sleepTime = eval(input("输入倒数时间"))
for i in range(sleepTime, 0, -1):
    print("%2d" % i, end="")  # 格式化输入，保证每一个数字都是两个位
    # print("Start : %s" % time.ctime())
    for v in range(i):
        print("*", end="")  # 嵌套打印星号
    else:
        print()
        time.sleep(1)
        # print("End : %s" % time.ctime())
print("time's up")
