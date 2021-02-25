#Functions

def gambling_implications(question):
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

def gambling_implications_instructions():
    print("*****Gambling Implications*****")
    print()
    print()
    print()
    print()
    return""

#Main Routine

show_gambling_implications = gambling_implications("Do you undertand the implications of gambling?")

if show_gambling_implications == "yes":
    print("Ask user if they have played before")

else:
    gambling_implications_instructions()

