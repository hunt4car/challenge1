nums = [2,4,6,8]
def squareEach(listOfNums):
    for i in range(len(listOfNums)):
        square = listOfNums[i]*listOfNums[i]#multiplys num by itself
        nums[i] = square #puts number, post calc into the same spot in the list it was before...squared now
        
squareEach(nums)#the actual funning of the program with list in use

print(nums)#prints list after it has been reworked into squared version
