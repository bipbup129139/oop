"""
class MyClass:
    name = "Test"

    #Konstruktors
    def __init__(self):
        pass

    #Metode
    def getName():
        return name

#programma
"""
"""
class Color:
    red = 0
    green = 0
    blue = 0

    def    __init__(self, r,g,b):
        self.red=r
        self.green=g
        self.blue=b
        print(r,g,b)

    def info_print(self, r,g,b):
        print(f'Red {r} green {g} blue {b}')

    def toHex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)
    
    def redColor(self):
        self.red=255
        for i in range(20):
            print(self.red-i, self-green, self.blue)

gray = Color(0,128,0)        
gray.info_print(0,128,0)
print(gray.toHex())
print(gray.redColor())
"""
"""
class Rectangle:
    def __init__(self):
        self.width=int(input("ievadiet platumu: "))
        self.height=int(input("ievadiet garumu: "))
       

rect1=Rectangle()

print(f"{rect1.width}x{rect1.height}")

rect2=Rectangle()
print(f"{rect2.width}x{rect2.height}")
"""

class Rectangle:
    def __init__(self, name, width=10, height=20, color='blue'):
        self.width=width
        self.height=height
        self.color=color
        self.name=name

    rect1=Rectangle("Square",100,200,"Orange")
    print(f"{rect1.color}{rect1.name}{rect1.width}x{rect1.height}")

    rect2=Rectangle('Rect')
    print(f"{rect2.color}{rect2.name}{rect2.width}x{rect2.height}")
rectangles=[]
for i in range(100):
    rectangles.append(Rectangle(f"Name{i+1}"))
print(len(rectangles))









