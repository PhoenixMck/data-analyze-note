# time库：处理时间的库，内置库，需要import
import time as t
# 【常命名为t】
# 处理时间【获取时间】的四个函数：time()获取当前时间戳【以1970年1月1日00:00为起始开始计时所计算的时间，一个以秒为单位，会返回一个浮点数】
# gmtime()获取当前时间戳对应北京时间的struct_time对象
# localtime()获取当前时间戳对应的本地时间的struct_time对象,跟gmtime的参数都是当前时间戳
# ctime()获取当前时间戳并返回一个可读的时间字符串
# gmtime他们返回的是计算机可处理的时间格式，把年月日当参数那种
print(t.time())
print(t.gmtime(t.time()))
print(t.localtime(t.time()))
print(t.gmtime(t.time()))
# 时间格式化，如strftime(tpl,ts)【格式符，对象】
# 就是用特定格式化控制符把时间用模板输出
# 年%Y，月：%m用数字表示，%B用英文全拼表示，%b用英文缩写表示
# 日：%d，小时：%H 24小时制，%I 12小时制，
# 上午、下午：%p，%M分钟，%S秒，
# 星期几：%A 英文全拼，%a英文缩写,
# 要写成字符串噢
"""
%Y 四位数的年份表示(000-9999)
%m 月份(01-12)
%d 月内中的一天(0-31)
%H 24小时制小时数(0-23)
%I 12小时制小时数(01-12)
%M 分钟数(00=59)
%S 秒(00-59)
"""
T = t.gmtime(t.time())
print(t.strftime("%Y:%m:%d:%H:%M:%S（%A）", T))#参数要是计算机的时间变量，而time返回的是一个浮点数
# 程序计时：测/度过时间两类。测量时间函数perf_counter()，获取CPU以其频率运行的时钟，是以纳秒来计算的，产生时间函数sleep()，它可以让程序休眠或产生一段时间。
start_time = t.perf_counter()
end_time = t.perf_counter()
spend_time = start_time - end_time
print(spend_time)
# sleep(秒数)参数为要跳过的秒数
t.sleep(2)