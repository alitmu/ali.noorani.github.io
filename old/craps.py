# To install the Colorama package, you can use "pip install colorama" command in terminal.
from colorama import Back, Style
import random
totalRound = 0

print(Back.GREEN + 'WELCOME TO CRAPS!')

ans = input(
    "Type ROLL or 1 to begin, QUIT or 2 to exit.")
ans = ans.upper()

while ans != "QUIT" and ans != "2":
    if ans == "ROLL" or ans == "1":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sum = dice1+dice2
        totalRound = totalRound+1

        print("Dice 1: ", dice1)
        print("Dice 2:", dice2)
        print("Total :", sum)

        if sum == 7 or sum == 11:
            print("Congratulations! You win!")
            print("Total number of rounds: ", totalRound)
            break
        elif sum == 2 or sum == 3 or sum == 12:
            print(Back.RED+"Oops! You LOSE!")
            print("Total number of rounds: ", totalRound)
            break
        else:
            ans = input(
                "You get another try. Type ROLL or 1 to begin, QUIT or 2 to exit.")
            ans = ans.upper()
            print("\n")
    else:
        ans = input(
            "Your input is not recognized. Type ROLL or 1 to begin, QUIT or 2 to exit.")
        ans = ans.upper()
