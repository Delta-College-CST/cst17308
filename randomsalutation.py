# This program generates a random salutation.

def sayMessage():
    import random
    selection = random.randrange(0, 5)
    if selection == 0:
        returnMsg = "Hey"
    elif selection == 1:
        returnMsg = "Yo"    
    elif selection == 2:
        returnMsg = "Wazzup"    
    elif selection == 3:
        returnMsg = "How goes it?"
    elif selection == 4:
        returnMsg = "Howdee"
    return returnMsg

print(sayMessage())
