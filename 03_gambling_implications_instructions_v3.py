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
            print()
            print("<error> please answer yes/no")
            print()

#gambling implication instructions, this will appear if user answers no to if they understand gambling implications.
def gambling_implications_instructions():
    print("*****Gambling Implications*****")
    print("Harm from gambling is not solely just losing money.")
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
gambling_implications_instructions()
print()
show_gambling_implications = gambling_implications("Do you understand the implications of gambling?")

#If user answers yes, program continues
#If user answers no, show gambling implications instructions and ask question again
while show_gambling_implications == "no":
    gambling_implications_instructions()
    print()
    show_gambling_implications = gambling_implications("Do you understand the implications of gambling?")


print("program continues")




