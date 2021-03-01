played_before = ""
while played_before.lower() != "xxx":
    #Ask user if they have played before
    played_before = input("Have you played before?").lower()
    #If user says yes, output 'program continues'
    if played_before == "yes":
        print("program continues")

    elif played_before == "y":
        print("program continues")

    #If user says no, output 'game information'
    elif played_before == "no":
        print("display game information")

    elif played_before == "n":
        print("display game information")

    #If user says maybe or any other word 'output <error> answer yes/no'
    else:
        print("<error> please answer yes/no")
