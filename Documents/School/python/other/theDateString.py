def main():
    
    months = "JanFebMarAprMayJunJulAugSepOctNowDec"
    theMonth = eval(input("Enter the number of the month: "))
    start = (theMonth-1)*3
    monthAbbrev = (months[start:start])
    print(monthAbbrev)
main()
