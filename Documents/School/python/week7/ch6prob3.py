from math import *
def sphereArea(radius):
    eval(input("Enter the radius of a sphere to get its area: "))
    area = (4* pi)*(radius**2)
    return area

def sphereVolume(radius):
    eval(input("Enter the radius of a sphere to get its volume: "))
    area = (4/3* pi)*(radius**3)
    return area

print("The area is: ",sphereArea(5))
print("The volume is: ",sphereVolume(5))
