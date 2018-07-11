from turtle import Turtle
default_scale = 10


def init_drawman():
    global t, x_current, y_current, _drawman_scale
    t = Turtle()
    t.penup()
    x_current = 0
    y_current = 0
    t.goto(x_current, y_current)
    drawman_scale (default_scale)

def init_coordinate_grid_axis():
    """
    иниициализирует черепах для пострения
    координатных осей и сетки
    :return:None
    """

    global t1, t2
    t1 = Turtle() #Координатные оси
    t1.width(2)
    t1.ht()
    t1.speed(100)
    t1.penup()

    t2 = Turtle() #Координатная сетка
    t2.width(0.5)
    t2.color("DarkGray")
    t2.ht()
    t2.speed(0)
    t2.penup()

def coordinate_grid_axis():
    coordinate_axis()
    coordinate_grid()

def coordinate_axis():
    vertical_axis(t1)
    horizontal_axis(t1)


def coordinate_grid():
    pass
    for i in range(-400, 401,_drawman_scale):
        vertical_axis(t2, i)
    for i in range(-300,300, _drawman_scale):
        horizontal_axis(t2, i)

def vertical_axis(turtl, axis = 0):
    turtl.goto(axis, 300)
    turtl.pendown()
    turtl.goto(axis, -300)
    turtl.penup()

def horizontal_axis(turtl, axis = 0):
    turtl.goto(400, axis)
    turtl.pendown()
    turtl.goto(-400, axis)
    turtl.penup()


def drawman_scale(scale):
    """
    Создает глобальную переменную
    для масштаба
    :param scale:
    :return: None
    """
    global _drawman_scale
    _drawman_scale = scale


def test_drawman():
    """
    Тестирование работы черчежника
    :return: None
    """
    pen_down()
    for i in range(5):
        on_vector(10, 20)
        on_vector(0, -20)
    pen_up()
    to_point(0, 0)



def pen_down():
    t.pendown()

def pen_up():
    t.penup()

def on_vector(dx, dy):
    to_point(x_current + dx, y_current + dy)

def to_point(x, y):
    global x_current, y_current
    x_current = x
    y_current = y
    t.goto(_drawman_scale*x_current, _drawman_scale*y_current)


init_drawman()
init_coordinate_grid_axis()
if __name__ == '__main__':
    import time
    test_drawman()
    time.sleep(5)

