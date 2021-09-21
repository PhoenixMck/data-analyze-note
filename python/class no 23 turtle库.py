from turtle import *
import time as t

"""
turtle库可以理解为有一个小海龟在坐标系中爬行，其轨迹就是最后呈现的图形
有前进、后退、旋转几种方式
起始位置为（0，0），方向为前进【右方】，前进方向为右方，上方方向是左侧，下方方向为右侧，左方方向为后退
"""
setup(1000, 1000, 100,100)  # 设计窗体，参数width窗口宽度【如果是整数直接就是像素，如果是小数就是窗口跟屏幕的比例】、height【窗口高度】、startx【窗口左侧离屏幕左侧的距离，若为None则居中】、starty【窗口顶部离屏幕顶部的距离，若为None则居中】
circle(100, 90, 4)  # 半径为正表示顺时针画圆，半径为负表示逆时针画圆,向下画圆
circle(80, 360, 3)  # n段线，从起点画360度回到起点==画一个正n边形
circle(70, 360, 4)
circle(50)  # 用来画弧度函数，参数radius【半径】、extent【圆心角，圆心角为负时顺小海龟当前方向画圆，负时则逆方向画，为None则画整圆】、steps【从起始到结束有多少条线】，圆心坐标是（0，radius）
penup()  # 拿起画笔，拿起画笔后turtle不会再作画,仍然可以移动，有轨迹就是没有墨迹，别名pu()\up()
pendown()  # 则相反
pensize(3)  # 设置画笔尺寸，若没有填入参数就返回当前画笔尺寸
pencolor("red")  # 设置颜色，参数是颜色的字符串或者（r,g,b）元组
circle(100)
# 填充颜色
color("blue", "red")  # 可以设置画笔和填充的颜色。两个参数【两个字符串或者两个RGB元组】，第一个是画笔颜色，第二个是填充颜色
begin_fill()  # 在填充前调用，不用输入颜色参数
circle(20)
goto(50, 50)  # 移动到绝对坐标（x,y），接下来的动作，把（x，y）作为原点，会产生一段轨迹
circle(30, 360, 5)
print(filling())  # filling返回当前图形的填充状态，有填充则为ture，无填充则为false
end_fill()  # 与begin搭配使用，表示后续图形不再使用fill，但画笔颜色不变，要有end颜色才会填上
print(filling())
# screensize设置画布窗口的宽度、高度【像素为单位】和背景颜色【字符串或者RGB元组】
screensize(1000, 1000, "black")
# 清空
clear()  # 清空当前画布，但不改变画笔坐标
circle(30)
reset()  # 清空画布同时回到原点,颜色等格式设置也还原了
# 隐藏画笔形状（把那个三角形去掉）
hideturtle()  # 无参数
# 显示画笔形状
showturtle()  # 无参数
# 显示画笔状态
print(isvisible())  # 画笔可见则返回ture
# 显示字符串 write(要显示的内容，font=（格式的元组:名称、尺寸、字体类型）)
screensize(1000, 1000, "White")
circle(20, 360, 2)
write("UKT", font=("Arial", 40, "normal"))  # 写完turtle回到起点

# 运动
forward(100)  # 从当前位置当前方向向前移动，会留下轨迹,别称为fw（）
pencolor("red")
pensize(5)
forward(-200)  # 负号代表反向运动
pencolor("black")
pensize(2)
back(100)  # 从当前位置向后移动，会留下轨迹，别称为bk()
right(90)  # 把当前坐标系向右旋转angle角度
back(100)
left(180)
pencolor("red")
forward(200)
reset()
circle(50, 360, 3)
penup()
setx(100)  # 把坐标水平平移到绝对坐标x,会留下轨迹，配合penup与pendown即可
pendown()
circle(50, 360, 3)
penup()
sety(100)  # 把坐标垂直平移绝对坐标y,会留下轨迹
pendown()
circle(50, 360, 3)
setheading(60)  # 设置当前朝向为angle的角度
circle(-50, 360, 3)
penup()
home()  # 回到为原点，朝向为东
pendown()
dot(5, "red")  # 设置一个圆点，第一个参数为半径，第二个为颜色
#返回位置
forward(50)
setheading(60)
forward(65)
print(position())#返回当前位置距离原点的距离
print(xcor())#返回当前x坐标
print(ycor())#返回当前y坐标
undo()  # 撤销上一个操作
speed(5)  # 设置绘画速度，0表示没有动作，1-10逐步增加速度，超过10相当于没有动作，相当于输入0
circle(-100, 360, 4)
t.sleep(2)  # 增加窗口停留时间
