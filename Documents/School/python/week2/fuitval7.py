def main():
    print("This program calculates an investments value over time")
    principal = eval(input("Enter the initial principal: "))
    yearRate = eval(input("What is your yearly rate: "))
    compound= eval(input("Enter how many times your compounded a year:"))
    years = 10

    for i in range (years * compound):
        principal = principal * (1+yearRate)
        print("period" ,i+1 ,principal)

    print("The value in year",years, "will be", principal)

main()

    
