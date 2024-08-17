# This program averages three test scores, determines
# if a student is passing or failing, and assigns
# a letter grade

# ---------------------------------------------------------

# Input action for individual tests
def inputTest(testNum):
    prompt = "Enter Test " + str(testNum) + " score: "
    testScore = int(input(prompt))
    return testScore

# Function to validate one test score
def scoreInvalid(score):
    invalid = False
    if score < 0 or score > 100:
        invalid = True
    return invalid

# Function to determine average of 3 valid test scores
def calcAveTestScore(t1,t2,t3):
    ave = (t1 + t2 + t3) / 3.0
    return ave

# Function to set error messsage.  Invokes scoreInvalid()
# function as needed.  Empty error message returned if all
# OK; otherwise, returns indications of which tests bad.
def checkTests(t1,t2,t3):
    errorMessage = "";
    if scoreInvalid(test1) == True:
        errorMessage += "Test 1 invalid\n"
    if scoreInvalid(test2) == True:
        errorMessage += "Test 2 invalid\n"
    if scoreInvalid(test3) == True:
        errorMessage += "Test 3 invalid\n"
    return errorMessage

# Function to convert grade average into string letter grade
def letterGrade(gradeAve):
    if average >= 90.0:
        gradeAve = "A"
    if average >= 80.0 and average < 90.0:
        gradeAve = "B"
    if average >= 70.0 and average < 80.0:
        gradeAve = "C"
    if average >= 60.0 and average < 70.0:
        gradeAve = "D"  
    if average < 60.0:
        gradeAve = "F"
    return gradeAve

# Function returns message indicating transferability of grade
def transferMsg(gradeAve):
    if gradeAve >= 73.0:
        message = "TRANSFER OK"
    else:
        message = "TRANSFER ISSUES"
    return message

# -------------------  MAIN ROUTINE  -----------------------

# Input two numbers
test1 = inputTest(1)
test2 = inputTest(2)
test3 = inputTest(3)

# Validate each test.  If variable errorMessage remains empty,
# all tests OK.  Otherwise, at least one is invalid, processing
# is skipped and an error message is indicated.
errorMessage = checkTests(test1,test2,test3)
    
print()  # Blank line

# Process valid tests
if errorMessage == "":
    
    # Calculate test average
    average = calcAveTestScore(test1, test2, test3)

    # Write test average and determine if student's grade will
    # transfer to a university.
    print ("Test Average: %5.1f" % (average))
    print(transferMsg(average))

    # Wite letter grade
    print("with a grade of: " + letterGrade(average))

else:  # If invalid, write error message
    
    print(errorMessage) 
    
# ---------------------------------------------------------


