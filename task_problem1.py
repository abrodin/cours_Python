from drawman import *
from time import sleep


drawman_scale(70)

coordinate_axis()

for i in 1,3:
    for k in range(1,5):
        to_point(i, k)
        point()

for y1 in range(1,5):
    for y2 in range(1,5):
        pen_up()
        to_point(1, y1)
        pen_down()
        to_point(3,y2)
pen_up()




sleep(10)