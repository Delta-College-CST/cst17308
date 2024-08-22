# This program prompts the user for a two character state code,
# validates it, and returns trivia related to the state.

# This function returns the "ordinality" of a number
def numberOrdinal(num):
    intNum = int(num)
    if intNum >= 11 or intNum <= 13:
        ordNum = num + "th"
    elif intNum % 10 == 1:
        ordNum = num + "st"
    elif intNum % 10 == 2:
        ordNum = num + "nd"
    elif intNum % 10 == 3:
        ordNum = num + "rd"
    else:
        ordNum = num + "th" 
    return ordNum

statefile = open("statefacts.txt", "r")        # Open file for reading

stateCodeChoice = input("Enter state code: ")  # Read target state

found = False    # For error checking

# Perform file processing loop until end
for line in statefile:

    # Read/split one line of state date
    code, name, nickname, capital, startdate, \
    enterNum, animal, bird, flower = line.split(",")

    # Determine ordinal number for state entry number 
    ordNum = numberOrdinal(enterNum)

    # Match state code - if matches, write all related info
    if stateCodeChoice == code:
        print("\n\n" + name)
        print("The",nickname)
        print("Capital:",capital)
        print("Entered U.S. on",startdate,"as the:",ordNum,"state")
        print("State Animal:",animal)
        print("State Bird:  ",bird)
        print("State Flower:",flower)

        found = True        # Mark that state was found

# If entire file traversed with no state code match, flag as error
if found == False:
    print("\n\nState not found.")


