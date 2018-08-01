class Vector2D:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def __add__(self, other):
        """
        :param other:
        :return: Сложение векторов
        """
        return Vector2D(self._x + other._x, self._y + other._y)

    def __mul__(self, other):
        """
        :param other:
        :return: Скалярное умножение векторов
        """
        return self._x*other._x, self._y*other._y


    def __str__(self):
        return '(%d, %d)' %(self._x, self._y)

a = Vector2D(2, 2)
b = Vector2D(-1, 2)
c = a + b
d = a*b
print(a, '+', b, '=', c)
print(a, '*', b, '=', d)