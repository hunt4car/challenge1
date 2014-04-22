#problem1 ch 7
def main():
    
    hoursWorked = eval(input("Enter the # of hours worked: "))
    wage = eval(input("Enter your hourly wage: $"))
    if hoursWorked > 40:
        pay = wage*40
        pay += (hoursWorked - 40)*(wage*1.5)
    else:
        pay = hoursWorked * wage

    print ("You earned : $", pay)
        
main()
