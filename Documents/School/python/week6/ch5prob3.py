from math import *
def main():
    grade = eval(input("enter your score (0-100): "))
    grades = ["f","f","d","c","b","a"]
    grade = round(grade/10)
    print (grades[grade])
main()
