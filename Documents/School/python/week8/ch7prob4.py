#ch7 prob4
from math import *
def main():
    creditsE = eval(input("Enter credits: "))

    status = "error"
    if (creditsE <=0) or (creditsE>=26):
        print ("Invalid input")
    else:
        if creditsE <= 7:
            status = "freshman"
        elif creditsE < 16:
            status = "sophomore"
        elif creditsE< 26:
            status = "junior"
        else :
            status = "senior"
        print ("the letter grade of",creditsE,"is: ",status)
        
main()
