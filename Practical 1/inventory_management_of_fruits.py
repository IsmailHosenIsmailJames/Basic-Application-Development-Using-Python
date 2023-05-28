# Lets inport CSV library
import csv

# Let's open a file for write data on a csv file.
file = open("fruitsData.csv", 'w')
csvWriter = csv.writer(file)

# Let's insert the header on csv file
csvWriter.writerow(["No.", "Fruits Name", "Per Unit Price", "Total Quantity", "Total Price"])

# Get input from user that how many fruits have there
while True:
    try:
        numberOfFruits = int(input("How many different types of do you have?  "))
    except ValueError:
        print("The numbers of fruits are not correct. Try again.")
        continue
    else:
        break

# Let's itreate numberOfFruits times for get full data
for itemNumber in range(numberOfFruits):
    fruitName = input("What is the name of Fruits? ")

    # get the price of fruits in per unit
    while True:
        try:
            perUnitPrice = float(input(f"What is the price of {fruitName} in per unit ?  "))
        except ValueError:
            print("This not correct number of price. Try again")
            continue
        else: break

     # get the quntity of total fruits
    while True:
        try:
            quntityOfFruits = float(input(f"What is the quntity of {fruitName}?  "))
        except ValueError:
            print("This not correct number of Quntity. Try again")
            continue
        else: break

    totalPrice = perUnitPrice * quntityOfFruits

    csvWriter.writerow([itemNumber+1, fruitName, perUnitPrice, quntityOfFruits, totalPrice])
    print("Successfully inserted data in file")

file.close()

print("All data stored in fruitsData.csv file")