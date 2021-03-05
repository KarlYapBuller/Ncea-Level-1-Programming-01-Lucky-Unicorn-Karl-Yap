#Functions

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
#gambling implication instructions, this will appear if user answers no to if they understand gambling implications.
def gambling_implications_instructions():
    print("*****Gambling Implications*****")
    print("Harm from gambling is not solely just losing money")
    print("Gambling can affect affect many aspects of a person's life such as")
    print("self-esteem, relationships, mental health and social life.")
    print("Gambling can cause extreme emotions and mood swings,")
    print("feeling that gambling is the only thing you can")
    print("enjoy;you can find other thing that are not gambling boring,")
    print("difficulty sleeping,have suicidal thoughts and")
    print("feel depressed or anxious.")
    print("Gambling does not only affect the gambler, but it can also affect ")
    print("the people around the gambler like their friends and family.")
    return""

#Main Routine
#Calls gambling implication functions
show_gambling_implications = gambling_implications("Do you undertand the implications of gambling?")

#If user answers yes, ask user if they have played before is run
if show_gambling_implications == "yes":
    print("program continues")

else:
    gambling_implications_instructions()
    print("program continues")
