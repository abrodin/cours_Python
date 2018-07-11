from drawman import *
from time import sleep

drawman_scale(10)
coordinate_grid_axis()

def f(x):
    return x*x

x = -5.0
to_point(x,f(x))
pen_down()
while x<=5:
    to_point(x,f(x))
    x += 0.1
pen_up()

sleep(5)