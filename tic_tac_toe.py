'''
Tic-tac-toe is a game played by two players on a 3x3 field where the duel takes place. One of the players plays as 'X',
and the other player is 'O'. 'X' plays first, then the 'O' side plays, and so on.
The first player that writes 3 'X' or 3 'O' in a straight line (including diagonals) wins.
'''


# Visualize different combinations that the user will determine from the input

moves = input('Enter cells: ')
cells = []

for move in moves:
    cells.append(move)

print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[-1], "|")
print("---------")

row0 = [cells[0], cells[1], cells[2]]
row1 = [cells[3], cells[4], cells[5]]
row2 = [cells[6], cells[7], cells[-1]]

col0 = [cells[0], cells[3], cells[6]]
col1 = [cells[1], cells[4], cells[7]]
col2 = [cells[2], cells[5], cells[-1]]

dia0 = [cells[0], cells[4], cells[-1]]
dia1 = [cells[2], cells[4], cells[6]]

combinations = [row0, row1, row2, col0, col1, col2, dia0, dia1]

win_count_x = 0
win_count_o = 0
blanks_count = 0
x_count = 0
o_count = 0

for combination in combinations:
    for cells in combination:
        if cells == "X":
            x_count += 1
        elif cells == "O":
            o_count += 1
        elif cells == "_":
            blanks_count += 1

# Loop to check for win counts
for combination in combinations:
    if combination[0] == combination[1] == combination[2] == "X":
        win_count_x += 1
    elif combination[0] == combination[1] == combination[2] == "O":
        win_count_o += 1

# Check the possible states of the game:
if win_count_x == 1 and win_count_o == 0:
    print('X wins')
elif win_count_o == 1 and win_count_x == 0:
    print('O wins')
elif win_count_x == 0 and win_count_o == 0 and blanks_count == 0:
    print("Draw")
elif (win_count_x == 1 and win_count_o == 1) or ((x_count - o_count) >= 2 or (o_count - x_count) >= 2):
    print("Impossible")

elif win_count_x == 0 and win_count_o == 0 and blanks_count > 0:
    print('Game not finished')

