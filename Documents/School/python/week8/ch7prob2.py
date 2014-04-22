#ch7 prob2
def main():
    numGrade = eval(input("Enter the # score: "))
    letterGrade = "error"
    if (numGrade <=0) or (numGrade >=5):
        print ("Invalid score, yo")
    else:
        if numGrade==0:
            letterGrade = "f"
        elif numGrade == 1:
            letterGrade = "d"
        elif numGrade == 2:
            letterGrade = "c"
        elif numGrade == 3:
            letterGrade = "b"
        elif numGrade == 4:
            letterGrade = "a"
        print ("the letter grade of",numGrade,"is: ",letterGrade)
        
main()
