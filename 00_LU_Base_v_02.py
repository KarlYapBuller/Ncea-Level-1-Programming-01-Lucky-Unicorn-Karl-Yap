#Functions

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
#Game information
def game_information():
    print("*****Game information*****")
    print()
    print("Rules of the game")
    print()
    print()
    return""

#Main Routine

show_played_before = played_before("Have you played this game before?")

if show_played_before == "no":
    game_information()

print("program continues")
