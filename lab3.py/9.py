import math
class circle:
    def __init__(self,radius):
        self.radius= radius
    

    def area(self):
        return math.pi * self.radius ** 2
    
r=int(input())
c=circle(r)
print(f"{c.area():.2f}")
