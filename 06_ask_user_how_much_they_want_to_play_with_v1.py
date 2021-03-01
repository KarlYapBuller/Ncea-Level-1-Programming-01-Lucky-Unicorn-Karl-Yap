#Functions go here



#Main Routine goes here

error = "Please enter a whole number between 1 and 10\n"

valid = False
while not valid:
    try:
        response = int(input("How much money would you like to play with? "))

        #If the amount is to low/to high give
        if 0 < response <= 10:
            print("You have asked to play with ${}".format(response))

        #Output an error
        else:
            print(error)

    except ValueError:
        print(error)

