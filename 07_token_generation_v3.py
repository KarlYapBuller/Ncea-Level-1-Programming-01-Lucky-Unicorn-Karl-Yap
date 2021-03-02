import random

#main routine goes here

tokens = ["Donkey", "Donkey", "Donkey", "Horse", "Horse", "Horse",
          "Zebra", "Zebra", "Zebra", "Unicorn"]
STARTING_BALANCE = 100

balance = STARTING_BALANCE

#Testing loop to generate 20 tokens
for item in range(0,100):
    chosen = random.choice(tokens)

    #Adjust balance of user
    if chosen == "Unicorn":
        balance += 4
    elif chosen == "Donkey":
        balance -= 1
    else:
        balance -= 0.5



#Output
print()
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))
