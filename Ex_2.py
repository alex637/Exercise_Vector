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
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)
    def __len__(self):
        return (self.x ** 2 + self.y ** 2)**0.5

n = int(input())
x = Vector(input())
Max, Max_len = x, x.__len__()
for i in range(1, n):
    x = Vector(input())
    if Max_len < x.__len__():
        Max, Max_len = x, x.__len__()
print('Радиус-вектор наиболее удалённой от начала координат точки ('+Max.__str__()+')')