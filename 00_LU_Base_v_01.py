#Working Luck Unicorn game

#Imports random number for odds of getting a specific token
import random

#Functions

#Gambling implications function, question asks the user if they understand the implications of gambling?
#If the user answers yes, program continues to the user if they have played before?
#If user answers no, gambling implications will display
#If user answers anyything other than yes/no, <error> please answer yes/no will appear
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
#gambling implication instructions, details to the user of the implications gambling has to the and society
#this will appear if user answers no to if they understand gambling implications.
def gambling_implications_instructions():
    print()
    print("Harm from gambling is not solely just losing money.")
    print("Gambling can affect affect many aspects of a person's life, such as")
    print("self-esteem, relationships, mental health and social life.")
    print("Gambling can cause extreme emotions, mood swings,")
    print("difficulty sleeping,suicidal thoughts,")
    print("depression or anxiousness.")
    print("Gamblers can often have the feeling ")
    print("that gambling is the only thing they can")
    print("enjoy;they can find other things that are not gambling boring,")
    print("Gambling does not only affect the gambler, but it can also affect ")
    print("the people around the gambler like their friends and family.")
    return""

#Played before function, output depends on what the user answers
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
def played_before(question):
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

#Game information function,
#Game information tells the user why the game is made (Doctors without Borders charity)
#Game rules and instructions
#This is displayed if user answers no, they have not played this game before
def game_information():
    statement_generator("Game information", "*")
    print()
    print("This game was created to raise money for the charity Doctors without Borders.")
    print("Doctors without Borders is an independant international medical")
    print("humanitarian orginisation that delivers emergency aid to")
    print("people affected by armed conflict, epidemics,")
    print("healthcare care exclusion and natural or man-made disasters.")
    print()
    print("*****Rules of the game*****")
    print("Choose a starting amount (minimum $1, maximum $10).")
    print()
    print("Then press <Enter to play>")
    print("You will either get a Donkey, Horse, Zebra or Unicorn token")
    print("The cost per round is $1.00")
    print()
    print("Depending on the token you may win some money back")
    print("Token payout amounts:")
    print("Unicorn: $5.00 (balance increases by $4.00)")
    print("Horse: $0.50 (balance decreases by $0.50)")
    print("Zebra: $0.50 (balance decreases by $0.50)")
    print("Donkey: $0.00 (balance decreases by $1.00)")
    print()
    print("If you want to quit the game while you are ahead "
          "type 'xxx' instead of typing <Enter>")
    print()
    print("Do you think you can get the "
          "Unicorns and walk home with the money?")
    print()
    return""

#Ask user how much they want to play for function
#Question is how much money do you want to play with
#User can only input a whole number betweeen 1 and 10
#If user does not enter a whole number between 1 and 10 error message is
#displayed telling the user to enter a whole numbe between 1 and 10
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

#Statement generator
#Decorates the statements in the Lucky Unicorn game
def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides , statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""

#Main Routine goes here
#Welcomes user to the Lucky Unicorn game, the
#"Welcome to the Lucky Unicorn game" statement is decorated
statement_generator("Welcome to the Lucky Unicorn game", "*")
print()

#The "Gambling implications" statement is decorated
statement_generator("Gambling implications", "?")
#Calls gambling implication functions
#Gambling implications instructions/information
#Gambling implications question
gambling_implications_instructions()
print()
show_gambling_implications = gambling_implications("Do you understand the implications of gambling?")
print()

#If user answers yes, program continues to ask user if they have played before?
#If user answers no, show gambling implications instructions and
#question is asked again until user answers yes
#If user answers anythoing other than yes/no <error> message is outputed
while show_gambling_implications == "no":
    gambling_implications_instructions()
    print()
    show_gambling_implications = gambling_implications("Do you understand the implications of gambling?")
    print()

#Calls ask user if they have played before funtion and game information function
#Played before statement is decorated
#If the user answers yes, program continues to ask the user how much they want to play with
#If user answers no, game information will display
#If user answers anything other than yes/no, <error> please answer yes/no will appear
print()
statement_generator("Played before", "?")
show_played_before = played_before("Have you played this game before?")
print()

if show_played_before == "no":
    print()
    game_information()

#Ask user how much they want to play with
#How much money do you want to play with statement is decorated
#User can only input a whole number between 1 and 10
#If user does not input a whole number between 1 and 10,
#<error> message will be outputed and user will be asked to input a whole number between 1 and 10
#Once user has inputed a correct value the amount the user has chosen to spend,
#will be outputed and displayed to the user
print()
statement_generator("Let us get started", "$")
how_much = number_check("How much money would you like to play with? ", 0, 10)
#Prints out amount user has chosen to play with
print("The amount you have chosen to spend is ${}".format(how_much))
print()

#Round looping
#User balance depends on how much the user has chosen to spend in the Lucky Unicorn game
balance = how_much

rounds_played = 0

#.lower is used just in case user types in exit code, 'xxx' in uppercase
#User presses <Enter to play and continue playing
#User inputs 'xxx' to quit the game
play_again = input("Press <Enter> to play").lower()
while play_again == "":

    #Increase rounds played by 1 each time user presses <Enter>
    #rounds played
    rounds_played += 1

    #Print number of rounds played
    #Rounds played statement decorator
    print()
    statement_generator("Round #{}".format(rounds_played), ".")
    print()
    #Chosees a random number between 1 and 10 and depending on that
    #number is the token the user will get
    chosen_number = random.randint(0,100)

    #Adjust balance of user
    #if the random #is between 1 and 5
    #User gets a Unicorn (add $4 to balance)
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        prize_decoration = "!"
        balance += 4

    #If the random #is between 6 and 36
    #User gets a Donkey (subtract $1 from balance)
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        prize_decoration = "D"
        balance -= 1

    #Token is either a Horse or Zebra
    #If user gets either a Horse or Zebra (subtract $0.50 from balance)
    else:
        #If number is even token generated is a Horse
        #Chosen item is Horse
        if chosen_number % 2 == 0:
            prize_decoration = "H"
            chosen = "Horse"
        #If number is not even token generated is a Zebra
        #Chosen item is a Zebra
        else:
            chosen = "Zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = ("You got a {}. Your balance is ${:.2f} ".format(chosen,balance))

    #Token/prize statement decorator
    statement_generator(outcome, prize_decoration)

#If balance is less than one program displays sorry you have run out of money
#User can choose if they want to continue the game or quit the game
#Sorry you have run out of money statement decorator
    if balance < 1:
        play_again = "xxx"
        print()
        statement_generator("Sorry you have run out of money", "^")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit game")
        print()
#Results statement is decorated, users final balance and thanks the user for playing Lucky Unicorn
print()
statement_generator("Results", "-")
print("Final balance ${:.2f}".format(balance))
print()
print("Thank you for playing Lucky Unicorn.")
print("Your money spent is for a good cause.")
print("You helped contribute to the charity, Doctors without Borders.")
print("Spread the word about this game and charity.")
print("Tell your friends, family and anyone you")
print("know, so we can help support the brave Doctors.")
print("We hope you will play again. ")



