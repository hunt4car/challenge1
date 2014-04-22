

def acronym_phrase():
    acc = ""
    phrase = input("Give a phrase: ")
    words = phrase.split()
    for each_word in words:
        acc = acc+each_word[0]
    print (acc.upper())
        
acronym_phrase() 
