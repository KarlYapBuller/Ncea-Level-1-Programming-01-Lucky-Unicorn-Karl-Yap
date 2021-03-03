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
    print("This game was created to raise money for the charity Doctors without Borders")
    print("Doctors without Borders is an independant international medical")
    print("humanitarian orginisation that delivers emergency aid to")
    print("people affected by armed conflict, epidemics,")
    print("healthcare care exclusion and natural or man-made disasters")
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
    return""

#Main Routine

show_played_before = played_before("Have you played this game before?")

if show_played_before == "no":
    game_information()

print("program continues")
