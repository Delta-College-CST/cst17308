# This program lists a variety products along with the
# customer reviews.

def getBarString(number):
    barChart = ""
    for i in range (0,number):
        barChart = barChart + "*"
    return barChart

# Write heading
print("PRODUCT                REVIEW")        

datafile = open("products.txt", "r")   # Open file for input

# Process product file one at a time
for line in datafile:

    # Read one line of data - one product and split out data
    prodNum, prodName, ratingStr = line.split(",")

    # Convert rating:  string --> integer
    rating = int(ratingStr)

    # Concatenate product number to end of product name
    prodName = prodName + " (" + prodNum + ")"

    # Call function to create rating histogram
    reviewBar = getBarString(rating)

    # Write one line of output
    print ("%-21s  %-5s" % (prodName, reviewBar))