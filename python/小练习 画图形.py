from turtle import *
import time as t

"""
同一起点同边长（50个像素）画n边形
"""

for num in range(3, 13):
    """画n边形"""
    per_angle = 360 / num
    for i in range(0, num):
        angle = per_angle * i
        setheading(angle)
        forward(50)

reset()
"""
以该图形的最后一条边作为下一个图形的第一条边
"""
end_angle = 0
for num in range(3, 12):
    """画n边形"""
    per_angle = 360 / num
    start_angle = end_angle
    for i in range(0, num):
        angle = start_angle + per_angle * i
        setheading(angle)
        forward(50)
    else:
        end_angle = angle + 180

t.sleep(2)
