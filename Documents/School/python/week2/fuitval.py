def main():
    print("This program calculates an investments value over time")
    principal = eval(input("Enter the initial principal:"))
    apr = eval(input("Enter the annual interest rate:"))
    years = eval(input("Enter how many years ahead you would like to calculate:"))

    for i in range (years):
        principal = principal * (1+apr)
        print("year" ,i+1 ,principal)

    print("The value in year",years, "will be", principal)

main()

    
