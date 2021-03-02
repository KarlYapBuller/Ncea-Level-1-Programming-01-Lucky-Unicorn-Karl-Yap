#set for testing purposes
balance = 5

rounds_played = 0

#.lower is used just in case user types in exit code, 'xxx' in uppercase
play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    #Increase #rounds played
    rounds_played += 1

    #Print number of rounds played
    print()
    print("*****Round #{}*****".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

#If balance is less than one program displays sorry you have run out of money
#User can choose if they want to continue the game or quit the game
    if balance < 1:
        play_again = "xxx"
        print("Sorry you have run out of money")
    else:
        play_again = input("Press <Enter> to play again or 'xxx' to quit game")

    print()
    print("Final balance", balance)
