class Quadrilateral:

    def __init__(self, width, height=None):
        self.height = height or width
        self.width = width

    def __str__(self):
        if bool(self):
            return f'Куб размером {self.width}х{self.width}'
        else:
            return f'Прямоугольник размером {self.width}х{self.height}'

    def __bool__(self):
        return self.width == self.height

q1 = Quadrilateral(10)
print(q1)  # печатает "Куб размером 10х10"
print(bool(q1))  # печатает "True"
q2 = Quadrilateral(3, 5)
print(q2)  # печатает "Прямоугольник размером 3х5"
print(q2 == True)  # печатает "False"