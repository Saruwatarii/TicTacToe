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

user_move = input("Enter the coordinates: ")

while True:

    if user_move[0].isdigit() and user_move[2].isdigit():
        break
    else:
        print("You should enter numbers!")
        user_move = input("Enter the coordinates: ")
        True

higher = False

while True:
    if int(user_move[0]) > 3 or int(user_move[2]) > 3:
        print("Coordinates should be from 1 to 3!")
        user_move = input("Enter the coordinates: ")
        True
    else:
        break

flag = True
while flag:

    if user_move == "1 3":
        if cells[0] == "X" or cells[0] == "O":
            print("This cell is occupied! Choose another one!")
            flag
            user_move = input("Enter the coordinates: ")
        elif cells[0] != "X" or cells[0] != "O":
            cells[0] = "X"
            flag = False

    if user_move == "1 2":
        if cells[3] == "X" or cells[3] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[3] != "X" or cells[3] != "O":
            cells[3] = "X"
            flag = False

    if user_move == "1 1":
        if cells[6] == "X" or cells[6] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[6] != "X" or cells[6] != "O":
            cells[6] = "X"
            flag = False

    if user_move == "2 1":
        if cells[7] == "X" or cells[7] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[7] != "X" or cells[7] != "O":
            cells[7] = "X"
            flag = False
    if user_move == "2 2":
        if cells[4] == "X" or cells[4] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[4] != "X" or cells[4] != "O":
            cells[4] = "X"
            flag = False

    if user_move == "2 3":
        if cells[1] == "X" or cells[1] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[1] != "X" or cells[1] != "O":
            cells[1] = "X"
            flag = False

    if user_move == "3 1":
        if cells[-1] == "X" or cells[-1] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[-1] != "X" or cells[-1] != "O":
            cells[-1] = "X"
            flag = False

    if user_move == "3 2":
        if cells[5] == "X" or cells[5] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[5] != "X" or cells[5] != "O":
            cells[5] = "X"
            flag = False

    if user_move == "3 3":
        if cells[2] == "X" or cells[2] == "O":
            print("This cell is occupied! Choose another one!")
            user_move = input("Enter the coordinates: ")
            flag
        elif cells[2] != "X" or cells[2] != "O":
            cells[2] = "X"
            flag = False


print("---------")
print("|", cells[0], cells[1], cells[2], "|")
print("|", cells[3], cells[4], cells[5], "|")
print("|", cells[6], cells[7], cells[-1], "|")
print("---------")



'''
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

'''