from turtle import *
import time as t

"""
同一起点同边长（50个像素）画n边形
"""

for num in range(3, 13):
    home()
    """画n边形"""
    per_angle = 360 / num
    for i in range(0, num):
        angle = per_angle * i
        setheading(angle)
        forward(50)
t.sleep(2)
