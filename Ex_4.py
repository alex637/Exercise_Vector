class Vector:
    def __init__(self, a=None, b=None):
        if b != None:           #  b!=None
            self.x = float(a)
            self.y = float(b)
        else:           #  b=None -> a is string 'x,y'
            self.x = float(a[:a.find(',')])
            self.y = float(a[a.find(',')+1:])
    def __str__(self):
        return str(self.x)+','+str(self.y)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __len__(self):
        return (self.x ** 2 + self.y ** 2)**0.5
    def __collin__(self, other):
        return True if self.x * other.y == self.y * other.x else False

n = int(input('Введите количество точек, затем точки в формате "x,y":  '))
A = []
for i in range(n):
    A.append(Vector(input()))

assert n >= 3
p_max = 0
for x in A[:n-2]:
    for y in A[1:n-1]:
        for z in A[2:]:
            a = x - y
            b = y - z
            c = z - x
            if not Vector.__collin__(a, b):
                p = a.__len__() + b.__len__() + c.__len__()
                if p > p_max:
                    p_max = p
if p_max == 0:
    print('Треугольник не существует')
else:
    print('Наибольший периметр равен ', p_max)