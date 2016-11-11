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

a = Vector(input())
b = Vector(input())
print('a + b = ', (a+b).__str__())
print('a * 2 = ', (a * 2).__str__())
print('2 * a = ', (2 * a).__str__())