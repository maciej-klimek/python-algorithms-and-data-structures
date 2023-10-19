import math

class triangle:
    def __init__(self, a, b, c):
        self.isTriangle = False
        self.a = a
        self.b = b
        self.c = c
        if a+b>=c and b+c>=a and c+a>=b:
            self.isTriangle = True
        
        if self.isTriangle:
            print("Jest to trójkąt")
        else:
            print("Nie jest to trójkąt")
    
    def __calcArea__(self):
        if self.isTriangle:
            s = (self.a + self.b + self.c) / 2  
            print((s*(s-self.a)*(s-self.b)*(s-self.c)) ** 0.5)
        else:
            print("Nie można wyonać operacji")
    
    def __calcCirc__(self):
        print(self.a + self.b + self.c)

class square:
    def __init__(self, a):
        self.a = a

    def __calcArea__(self):
        print(self.a**2)
    
    def __calcCirc__(self):
        print(4*self.a)

class circle:
    def __init__(self, r):
        self.r = r

    def __calcArea__(self):
        print(f"{math.pi * self.r**2} = {self.r**2}pi")

    def __calcCirc__(self):
        print(f"{math.pi * self.r * 2} = {2*self.r}pi")


#triangle(1, 10, 1).__calcArea__()
square(4).__calcCirc__()