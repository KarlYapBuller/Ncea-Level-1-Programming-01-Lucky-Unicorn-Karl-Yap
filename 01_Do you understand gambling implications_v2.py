
show_gambling_implications = ""
while show_gambling_implications.lower() != "xxx":
    #Ask user if they understand the implications of gambling
    show_gambling_implications = input("Do you understand the implications of Gambling?").lower()
    #If user says yes, output 'ask user if they have played before'
    if show_gambling_implications == "yes" or show_gambling_implications == "y":
        show_gambling_implications = "yes"
        print("Ask user if they have played before?")

    #If user says no, output 'display gambling implications'
    elif show_gambling_implications == "no" or show_gambling_implications == "n":
        show_gambling_implications = "no"
        print("Display gambling implications")

    #If user says maybe or any other word 'output <error> answer yes/no'
    else:
        print("<error> please answer yes/no")
