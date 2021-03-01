
played_before = ""
while played_before.lower() != "xxx":
    #Ask user if they have played this game before
    played_before = input("Have you played this game before?").lower()
    #If user says yes, output 'program continues'
    if played_before == "yes" or played_before == "y":
        played_before = "yes"
        print("program continues")

    #If user says no, output 'display game information'
    elif played_before == "no" or played_before == "n":
        played_before = "no"
        print("Game information")

    #If user says maybe or any other word 'output <error> answer yes/no'
    else:
        print("<error> please answer yes/no")
