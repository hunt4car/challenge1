def main():
    print("This program converts celcius to fahrenheit (5 times)! YAY!")
    for i in range (5):
        celcius = eval(input("enter the temp in celcius: "))
        fahrenheit = 9/5 * celcius + 32
        print ("the temp in fahrenheit is ",fahrenheit)

main()
