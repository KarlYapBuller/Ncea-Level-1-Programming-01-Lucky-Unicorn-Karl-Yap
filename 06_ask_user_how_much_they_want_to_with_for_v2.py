#Functions goes here
def number_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            #Ask the question
            response = int(input(question))

            #If the amount is to low/to high give
            if low < response <= high:
                return response

            #Output an error
            else:
                print(error)

        except ValueError:
            print(error)

#Main routine goes here
how_much = number_check("How much money would you like to play with? ", 0, 10)

#Prints out amount user has chosen to play with
print("The amount you have chosen to spend is ${}".format(how_much))
