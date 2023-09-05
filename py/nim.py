# nim.py
# Warren Zeng
# CSCI 77800 Fall 2023
# collaborators: n/a
# consulted: n/a

import random

stones = 12

print("Welcome to the Game of Nim! There are 12 stones in a bag. The winner is the one that takes the last stone out! \n")
print("There are 12 stones remaining.\n")

while(stones != 0):
    
    user_choice = int(input("How many stones would you like to remove?: \n"))
    while (user_choice < 1 or user_choice >3 or user_choice > stones):
        user_choice = int(input("Please enter a number between 1 and 3 that is not greater than the number of stones remaining. \n"))
    stones = stones - user_choice

    print("There are", stones, "stones remaining.\n")
    if (stones == 0):
        print("Player wins!")
    
    computer_choice = random.randint(1,3)
    while(computer_choice > stones):
        computer_choice -= 1 
    print("Computer removes", computer_choice, "stone(s).")
    stones = stones - computer_choice
    print("There are", stones, "stones remaining.\n")

    if (stones == 0):
        print("Computer wins!")
