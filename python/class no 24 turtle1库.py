from turtle import *

"""
turtle库可以理解为有一个小海龟在坐标系中爬行，其轨迹就是最后呈现的图形
有前进、后退、旋转几种方式
起始位置为（0，0），方向为前进【右方】，前进方向为右方，上方方向是左侧，下方方向为右侧，左方方向为后退
"""
#setup(10000,10000) # 设计窗体，参数width窗口宽度【如果是整数直接就是像素，如果是小数就是窗口跟屏幕的比例】、height【窗口高度】、startx【窗口左侧离屏幕左侧的距离，若为None则居中】、starty【窗口顶部离屏幕顶部的距离，若为None则居中】
circle(100, 90, 4)
circle(50)  # 用来画弧度函数，参数radius【半径】、extent【圆心角，圆心角为负时顺小海龟当前方向画圆，负时则逆方向画，为None则画整圆】、steps【从起始到结束有多少条线】，圆心坐标是（0，radius）
penup()#拿起画笔，拿起画笔后turtle不会再作画，别名pu()\up()
pendown()#则相反
pensize(3)#设置画笔尺寸，若没有填入参数就返回当前画笔尺寸
pencolor("red")#设置颜色，参数是颜色的字符串或者（r,g,b）元组
circle(100)
