from drawman import *
from time import sleep

drawman_scale(30)
coordinate_grid_axis()

def f(x):
    return x**2 - 9

a = 0
b = 10
x = a
to_point(x,f(x))
pen_down()
while x<=b:
    to_point(x,f(x))
    x += 0.1
pen_up()


assert f(a)*f(b) < 0 #Функция должна быть знакопеременной на отрезке
while (b-a)/2 > 0.0000001:
    c = (a+b)/2
    if f(c)*f(a) < 0:
        b = c #a,b = a,c
    elif f(c) * f(a) > 0:
        a = c #a,b = c,b
    else:
        a,b = c

print('корень: ',(a+b)/2, '+-',(b-a)/2)

sleep(5)