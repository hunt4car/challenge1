#ch7 prob7
from math import *
def main():
    startHour = eval(input('Enter the starting hour: '))
    endHour = eval(input('Enter the end hour: '))

    if startHour < 21 and endHour < 21:
        totalTime = endHour - startHour
        totalRate = totalTime * 2.50
        print ('The total rate is : ', (totalRate))
        
    elif startHour >= 21:
        totalTime = endHour - startHour
        totalRate = totalTime * 1.75
        print ('The total rate is : ', (totalRate))
        
    elif startHour < 21 and endHour > 21:
        regRate = (21 - startHour) * 2.50
        dropTime = (endHour - 21) * 1.75
        totalRate = regRate + dropTime
        print ('The total rate is : ', (totalRate))
        

main()
