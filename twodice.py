# Function simulates throwing two dice
def throw2dice():
    import random
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1 + die2
    
diceThrow = throw2dice() # Make function call
print(diceThrow)         # Write results