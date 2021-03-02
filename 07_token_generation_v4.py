import random

#main routine goes here


STARTING_BALANCE = 100

balance = STARTING_BALANCE

#Testing loop to generate 10 tokens
for item in range(0,10):
    chosen_number = random.randint(0,100)

    #Adjust balance of user
    #if the random #is between 1 and 5
    #User gets a Unicorn (add $4 to balance)
    if 1 <= chosen_number <= 5:
        chosen = "Unicorn"
        balance += 4

    #If the random #is between 6 and 36
    #User gets a Donkey (subtract $1 from balance)
    elif 6 <= chosen_number <= 36:
        chosen = "Donkey"
        balance -= 1

    #Token is either a Horse or Zebra
    #If user gets either a Horse or Zebra (subtract $0.50 from balance)
    else:
        #If number is even token generated is a Horse
        #Chosen item is Horse
        if chosen_number % 2 == 0:
            chosen = "Horse"
        #If number is not even token generated is a Zebra
        #Chosen item is a Zebra
        else:
            chosen = "Zebra"
        balance -= 0.5



#Output
    print("You got a {}. Your balance is ${:.2f} ".format(chosen,balance))

print()

print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
