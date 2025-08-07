'''
-1 for water
1 for snake
0 for gun
'''

import random

computer = random.choice([-1, 0, 1])

youStr = input("Enter your choice: ")

youDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1:"snake", -1:"water",0:"gun"}
you = youDict[youStr]

print(f"you chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
  print("It's a draw")

elif (computer == 1 and you == -1) or \
      (computer == -1 and you == 0) or \
      (computer == 0 and you == 1):
  print("You lost")
else:
  print("You win")