# This program averages three test scores, determines
# if a student is passing or failing, and assigns
# a letter grade

# ------------------------------------------

# Method to validate one test score
def scoreInvalid(score):
    invalid = False
    if score < 0 or score > 100:
        invalid = True
    return invalid

# ------------------------------------------

# Input two numbers
test1 = int(input("Enter Test 1 score: "))
test2 = int(input("Enter Test 2 score: "))
test3 = int(input("Enter Test 3 score: "))

# Initialize to assume tests are valid.  
testsOK = True;
errorMessage = ""

# Validate each test.  Accumulate error messages for invalid input.
if scoreInvalid(test1) == True:
    testsOK = False
    errorMessage += "Test 1 invalid\n"
if scoreInvalid(test2) == True:
    testsOK = False
    errorMessage += "Test 2 invalid\n"
if scoreInvalid(test3) == True:
    testsOK = False
    errorMessage += "Test 3 invalid\n"
    
print()  # Blank line

# Process valid tests
if testsOK == True:
    # Calculate test average
    average = (test1 + test2 + test3) / 3.0

    # Write test average and determine if student's grade will
    # transfer to a university.
    print ("Test Average: %5.1f" % (average))
    if average >= 73.0:
        print("TRANSFER OK")
    else:
        print("TRANSFER ISSUES")

    # Wite letter grade
    print("with a grade of:")
    if average >= 90.0:
        print("A")
    if average >= 80.0 and average < 90.0:
        print("B")
    if average >= 70.0 and average < 80.0:
        print("C")
    if average >= 60.0 and average < 70.0:
        print("D")    
    if average < 60.0:
        print("F")
else:               # If invalid, write error message
    print(errorMessage) 
    
########################################################


