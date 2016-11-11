__author__ = 'student'
import math
class Vector:
    def __init__(self, a=None, b=None, c=None):
        if b != None:           #  b!=None -> a,b,c - coordinates
            self.x = float(a)
            self.y = float(b)
            self.z = float(c)
        else:                   #  b=None -> a is string 'x,y,z'
            self.x = float(a[:a.find(',')])
            self.y = float(a[a.find(',')+1:a.rfind(',')])
            self.z = float(a[a.rfind(',')+1:])
    def __str__(self):
        return str(self.x)+','+str(self.y)+','+str(self.z)
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)
    def __iadd__(self, other):
        self.x +=other.x
        self.y +=other.y
        self.z +=other.z
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.x*other.x + self.y*other.y + self.z*other.z
        else:
            return Vector(self.x * other, self.y * other, self.z * other)
    def __rmul__(self, const):
        return Vector(self.x * const, self.y * const, self.z * const)
    def __pow__(self, power, modulo=None):
        return Vector(self.y*power.z - self.z*power.y, self.z*power.x - self.x *power.z, self.x*power.y-self.y*power.x)
    def len(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2)**0.5
    def collin(self, other):
        if self.x * other.y == self.y * other.x and self.z * other.y == self.y * other.x:
            return True
        else:
            return False
    def angle(self, other):
        if self.len()*other.len() != 0:
            if Vector.collin(self, other):
                return 0
            else:
                return math.acos((self * other) / (self.len()*other.len()))
        else:
            return 'Один из векторов - нуль-вектор'
    def print(self, msg):
        print(msg+' '+'('+str(self)+')')


a = Vector(input())
b = Vector(input())
print('Скалярное произведение равно', str(a*b))
print('Угол между векторами в радианах:', Vector.angle(a,  b))
Vector.print(a**b, 'Векторное произведение')