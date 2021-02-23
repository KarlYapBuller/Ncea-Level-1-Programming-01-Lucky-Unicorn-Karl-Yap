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

#Main Routine

show_gambling_implications = gambling_implications("Have you played this game before?")
print("You choose {}".format(show_gambling_implications))
