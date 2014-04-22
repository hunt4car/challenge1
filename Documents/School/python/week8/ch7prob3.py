#ch7 prob3
from math import *
def main():
    numGrade = eval(input("Enter the # score: "))

    letterGrade = "error"
    if (numGrade <=0) or (numGrade >=100):
        print ("Invalid score, yo")
    else:
        if numGrade <= 60:
            letterGrade = "f"
        elif numGrade < 69:
            letterGrade = "d"
        elif numGrade < 79:
            letterGrade = "c"
        elif numGrade < 89:
            letterGrade = "b"
        else :
            letterGrade = "a"
        print ("the letter grade of",numGrade,"is: ",letterGrade)
        
main()
