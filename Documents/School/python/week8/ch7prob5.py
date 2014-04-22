#ch7 prob5
from math import *
def main():
    weight = eval(input("Enter body weight: "))
    height = eval(input("Enter body height: "))

    weightBMI = (weight * 720)
    heightBMI = sqrt(height)

    bmi = heightBMI / weightBMI

    if bmi>19 and bmi<25:
        print("your bmi is good")
    elif bmi<19:
        print("your bmi is low")
    else:
        print("your bmi is high")
    
    
        
main()
