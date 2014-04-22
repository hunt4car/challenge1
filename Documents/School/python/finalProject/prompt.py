def prompt():
    
#fallBack function that creates a default input for blank submissions during the user prompt

    from random import randint

    def fallBack(subType, submission):
        if not submission:
            return (subType[randint(1,len(subType)-1)])
        else:
            return submission

#end fallBack







#list of inputs per input type (to be used when no entry was given)

    names = ("Bob","Bruce","Brucie","BruciePoo","Ryan","ASAP Rocky", "Timmy", "Mom", "Dad", "Rando")
    feelings = ("sad","happy","confused","weird", "insane", "lost", "nice", "too nice")
    locations = ("Canada","Hell","Africa","Cape Horn", "Clark College", "Washington", "Oregon", "another dimension")
    actions = ("drumming","sking","skating","sleeping", "flying", "eating", "killing", "enhancing")

#END list of inputs






#random imput generator (for blank inputs)

    from random import randint
    
    #format:  randint(2,9) 

    #print(names[randint(0,len(names))])

#END random inout generator



#start user prompt (variables to be used in story)

    print("I am a MadLibs program, if at you do not enter a responce then a random word will be selected for you \n")
               
    name = fallBack(names,input("What is your name? \n"))

    location = fallBack(locations,input("Hi "+name+"! Nice to meet you, I live inside a computer, where do you live? \n"))
    feeling = fallBack(feelings,input("Interesting, I have never been too "+location+" what are the people like there? \n")) # "the man was" feeling
    #start finding animalName
    animalTest = input("I have been told that I am "+feeling+" aswell! I bet my pet mouse would agree with that, do you have any pets? (yes or no) \n").lower()
    if (animalTest == "yes"):
        animalNum = eval(input("Cool how many pets do you have? \n"))
        if animalNum == 1:
            animalName = fallBack(names,input("Whats the name of your pet? \n"))
        elif animalNum > 2:
            animalName = fallBack(names,input("Whats the name of your favorite pet? \n"))
        elif animalNum < 0 :
            print("I dont know how you could end up with ",animalNum," pets... and that worrys me \n")
            animalName = (names[randint(1,len(names)-1)])
        #else:
            #animalName("Ok thats a lot of pets! Whats the name of your favorite one?")
            #print("I like the name, "+animalName+"! Thanks for sharing that! Hmm, what else would I like to know...")
    elif (animalTest ==  "no"):
        print("Yeah pets can be a handful... \n")
        animalName = (names[randint(1,len(names)-1)])
    else:
        animalName = (names[randint(1,len(names)-1)])
        print("Your responce confuses me... umm... \n")
    #end finding animalName

    bestFriend = fallBack(names,input("Interesting...well out of your friends...who is your best friend? \n"))
    activity = fallBack(actions,input("You and "+bestFriend+" must have lots of fun together! What is your favorite activity to do with "+bestFriend+", like (i.e. running, golfing, surfing)... \n"))
    relitive = fallBack(names,input("Interesting... being a computer I have never got the chance to try "+activity+"... I dont have any family either... but you must, what's favorite relitives name? \n"))


    #now I have the variables: name, location, feeling, animalName, bestFriend, relitive

    print("You actually just picked a 'favorite relitive'! Haha, lets start with the mad libs before things start going downhill! \n")  

    return name,location,feeling,animalName,bestFriend,activity,relitive
#end user prompt
