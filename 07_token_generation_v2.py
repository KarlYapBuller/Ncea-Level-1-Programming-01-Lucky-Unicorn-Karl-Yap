import random

#main routine goes here

tokens = ["Donkey", "Horse", "Zebra", "Unicorn"]
balance = 100

#Testing loop to generate 20 tokens
for item in range(0,20):
    chosen = random.choice(tokens)

    #Adjust balance of user
    if chosen == "Unicorn":
        balance += 4
    elif chosen == "Donkey":
        balance -= 1
    else:
        balance -= 0.5



#Output
print("Token: {} , Balance: ${}".format(chosen, balance))
