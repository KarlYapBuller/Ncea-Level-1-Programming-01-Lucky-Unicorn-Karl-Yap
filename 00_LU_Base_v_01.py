#Functions

#Gambling implications function
def gambling_implications(question):
    valid = False
    while not valid:
        response = input(question).lower()
#If user response is either 'yes' or 'y' the response will be outputed as yes.
        if response == "yes" or response == "y":
            response = "yes"
            return response
#If user response is either 'no' or 'n' the response will be outputed as no.
        elif response == "no" or response == "n":
            response = "no"
            return response
#If user response is anything other than yes or no,user will be asked to answer yes or no.
        else:
            print("<error> please answer yes/no")
#gambling implication instructions, this will appear if user answers no to if they understand gambling implications.
def gambling_implications_instructions():
    print("*****Gambling Implications*****")
    print("Harm from gambling is not solely just losing money")
    print("Gambling can affect affect many aspects of a person's life such as")
    print("self-esteem, relationships, mental health and social life.")
    print("Gambling can cause extreme emotions and mood swings,")
    print("feeling that gambling is the only thing you can")
    print("enjoy;you can find other thing that are not gambling boring,")
    print("difficulty sleeping,have suicidal thoughts and")
    print("feel depressed or anxious.")
    print("Gambling does not only affect the gambler, but it can also affect ")
    print("the people around the gambler like their friends and family.")
    return""

#Played before function
def played_before(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "yes"
            return response

        elif response == "no" or response == "n":
            response = "no"
            return response

        else:
            print("<error> please answer yes/no")
#Game information function
def game_information():
    print("*****Game information*****")
    print("Doctors without borders")
    print("Rules of the game")
    print()
    print()
    return""

#Ask user how much they want to play for function
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

#Main Routine goes here

#Calls gambling implication functions
show_gambling_implications = gambling_implications("Do you undertand the implications of gambling?")

#If user answers yes, ask user if they have played before is run
if show_gambling_implications == "yes":
    print("Ask user if they have played this game before?")

else:
    gambling_implications_instructions()

#Calls ask user if they have played before funtionand game information
show_played_before = played_before("Have you played this game before?")

if show_played_before == "no":
    game_information()

print("program continues")

#Ask user how much they want to play with
how_much = number_check("How much money would you like to play with? ", 0, 10)

print("The amount you have chosen to spend is ${}".format(how_much))



