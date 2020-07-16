'''
Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place. One of the players plays as 'X',
and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.
The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.
'''


# Visualize different combinations that the user will determine from the input

interface = input("Enter cells: ")

print("---------")
print("| " + (interface[0]) + " " + (interface[1]) + " " + (interface[2]) + " |\n"
      "| " + (interface[3]) + " " + (interface[4]) + " " + (interface[5]) + " |\n"
      "| " + (interface[6]) + " " + (interface[7]) + " " + (interface[-1]) + " |")
print("---------")