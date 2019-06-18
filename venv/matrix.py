import random

class Matr:
    """Создает матрицу"""
    def __init__(self, x = 4, y = 4, n = 9):
        self.x = x
        self.y = y
        self.n = n
        self.matrica = []

        for i in range(0,self.y):
            stroka = []
            for j in range(0,self.x):
                stroka.append(random.randint(0,n))
            self.matrica.append(stroka)
        pass