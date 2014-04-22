from math import*

def pizzaArea(radius):
    area=pi*(radius **2)
    return area

def pricePerSqIn(area,PriceOfPizza):
    cost = PriceOfPizza / area
    return cost

print(pizzaArea(8))
print(pricePerSqIn(8,8))
