beer = eval(input("How much beer do you want to go through: "))
def song(num):
    while True:
        print (num, " bottles of beer on the wall, ",num, "bottles of beer. Take one down and pass it around, " ,num-1, " bottles of beer on the wall.")
        if num > 0: break

song(beer)

