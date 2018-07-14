import tkinter
from random import choice, randint

ball_initial_number = 20
ball_min_radius = 15
ball_max_radius = 40
ball_valid_color = ['green', 'blue','red', 'lightgray', '#FF00FF', '#FFFF00']


def click_ball(event):
    """
    Обработчик событий мышки для игрового холста
    :param event: событие с координатами клика
    По клику мышкой нужно удалять тот объект
    на который мышка указывает.
    А также засчитывает его в очки пользователя.
    """
    object = canvas.find_closest( event.x, event.y)
    x1, y1, x2, y2 = canvas.coords(object)
    if x1<= event.x <= x2 and y1 <= event.y <= y2:
        canvas.delete((object))
    # FIXME: нужно учесть объект в очках
    crefte_random_ball()


def move_all_balls(event):
    """
    Передвинает все шарики на чуть-чуть
    """
    for object in canvas.find_all():
        dx = randint(-1,1)
        dy = randint(-1,1)
        canvas.move(object, dx, dy)



def crefte_random_ball():
    """
    Создает шарик в случайном месте игрового холста canvas,
    при этом не выходит за границы холста!
    """
    R = randint(ball_min_radius, ball_max_radius)
    x = randint(0, int(canvas['width'])-1-2*R)
    y = randint(0, int(canvas['height'])-1-2*R)
    canvas.create_oval(x,y, x+2*R, y+2*R, width=1, fill=random_color())


def random_color():
    """
    :return: Случайный цвет из некоторого набора цветов
    """
    return choice(ball_valid_color)


def init_ball_catch_game():
    """
    Создает необходимое для игры количество шариков
    по которым нужно будет кликать
    """
    for i in range(ball_initial_number):
        crefte_random_ball()


def init_main_window():
    global root,canvas

    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, bg='PowderBlue',width=600, height=400 )
    canvas.bind("<Button>", click_ball)
    canvas.bind("<Motion>", move_all_balls)
    canvas.pack()


if __name__=="__main__":
    init_main_window()
    init_ball_catch_game()
    root.mainloop()
    print("Приходите играть ещё!")