import random

#set for testing purposes
balance = 5

rounds_played = 0

#.lower is used just in case user types in exit code, 'xxx' in uppercase
play_again = input("Press <Enter> to play").lower()
while play_again == "":

    #Increase #rounds played
    rounds_played += 1

    #Print number of rounds played
    print("*****Round#{}*****".format(rounds_played))

    chosen_number = random.randint(0,100)

    #Adjust balance of user
    #if the random #is between 1 and 5
    #User gets a Unicorn (add $4 to balance)
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        balance += 4

    #If the random #is between 6 and 36
    #User gets a Donkey (subtract $1 from balance)
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        balance -= 1

    #Token is either a Horse or Zebra
    #If user gets either a Horse or Zebra (subtract $0.50 from balance)
    else:
        #If number is even token generated is a Horse
        #Chosen item is Horse
        if chosen_number % 2 == 0:
            chosen = "Horse"
        #If number is not even token generated is a Zebra
        #Chosen item is a Zebra
        else:
            chosen = "Zebra"
        balance -= 0.5

    print("You got a {}. Your balance is ${:.2f} ".format(chosen,balance))

#If balance is less than one program displays sorry you have run out of money
#User can choose if they want to continue the game or quit the game
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit game")
        print()

print()
print("Final balance", balance)
