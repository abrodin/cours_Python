class A:
    class_level_list = ['1','2','2']

    def __init__(self, N):
        """
        N -- параметр масштаба. длина списка exemplar_list
        """
        self.exemplar_list = [x for x in range (N)]


a = A(5)
b = A(3)
a.x = 1
print('a.exemplar_list == b.exemplar_list', a.exemplar_list == b.exemplar_list )
print('a.exemplar_list is b.exemplar_list', a.exemplar_list is b.exemplar_list )
print('a.exemplar_list', a.exemplar_list )
print('b.exemplar_list', b.exemplar_list )