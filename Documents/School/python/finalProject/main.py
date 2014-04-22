#Final Project ctec121
#Madlibs program
#By: Hunter Nelson



def main():

    #this runs a series of questions in the structure of a short converstation, getting needed variables for a madlibs story
    import prompt 
    name,location,feeling,animalName,bestFriend,activity,relitive = prompt.prompt()

    #count down here?







    #stories

    story1 = "Once upon a time there was a elephant named "+name+" who was owned by a man named "+animalName+". In the city of "+location+" was the "+relitive+"'s zoo, it was here that "+name+" would spend each day "+activity+". Feeling "+feeling+" "+name+" decided to run off and chase his/her dreams of "+activity+". In sharing plans with "+bestFriend+" it became clear to "+name+" that it would be really hard to do this. So "+name+" decided to stay at the zoo. \n"   

    story2 = name+" was walking his pet named "+animalName+" through "+location+". When suddenly a wild "+relitive+" came out of nowhere! "+name+" reacted quickly by "+activity+", which made him/her feel "+feeling+" and they didnt want to be "+activity+" anymore. They called "+bestFriend+" who they showed up with a helicopter. So "+name+" lived to see another day \n"   

    #list of stories...

    stories = [story1, story2];

    storiesNum = len(stories)

    #print(storiesNum)

    def storyChoicePrompt():
        choice = eval(input('We have '+str(storiesNum)+' stories to choose from... pick one (enter a number 1-'+str(storiesNum)+')\n'))
        return choice


    def storyChoiceCheck():
        if (choice > storiesNum) or (choice < 0) or (choice==""):
            print("Errored input! Try again...")
            storyChoicePrompt()
            storyChoiceCheck()
        else:
            print ("\n",stories[choice-1])
            file = open("newfile.txt", "w")

            file.write(stories[choice-1])





                #actually have them pick the storie...

    choice = storyChoicePrompt()
    storyChoiceCheck()
main()


