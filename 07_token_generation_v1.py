import random

#main routine goes here

tokens = ["Donkey", "Horse", "Zebra", "Unicorn"]

#Testing loop to generate 20 tokens
for item in range(0,20):
    chosen = random.choice(tokens)
    print(chosen)
