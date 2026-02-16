import math
class Shape:
    def area(self):
        pass

class circle(Shape):
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return f"{math.pi*self.radius*self.radius:.2f}"

class rectangle(Shape):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def area(self):
        return self.length*self.width
    
class triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

print("1. Circle")
print("2. Rectangle")
print("3. Triangle")

ch=int(input("Enter shape: "))
if ch==1:
    r=float(input("Enter Radius: "))
    s=circle(r)
elif ch==2:
    l=float(input("Enter length: "))
    w=float(input("Enter width: "))
    s=rectangle(l,w)
elif ch == 3:
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    s = triangle(b, h)
else:
    print("Invalid choice")
    exit()

print("Area:", s.area())
        