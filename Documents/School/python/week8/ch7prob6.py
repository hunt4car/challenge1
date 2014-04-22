#ch7 prob6
from math import *
def main():
    speed = eval(input("Enter speed car was going: "))
    speedLimit = eval(input("Enter speed limit: "))
    over = speed - speedLimit

    if speed < 90:
        fine = (over* 5)+50
        print("your fine is: " ,fine+200)
    else:
        print("your fine is: ",fine)
    
    
        
main()
