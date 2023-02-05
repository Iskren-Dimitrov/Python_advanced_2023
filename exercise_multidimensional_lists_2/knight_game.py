'''3.	Knight Game
Chess is the oldest game, but it is still popular these days. It will be used only one chess piece for this task - \
the Knight.
A chess knight has 8 possible moves it can make, as illustrated. It can move to the nearest square but not on the same\
row, column, or diagonal. (e.g., it can move two squares horizontally, then one square vertically, or it can move one\
square horizontally then two squares vertically - i.e., in an "L" pattern.)
The knight game is played on a board with dimensions N x N.
You will receive a board with "K" for knights and "0" for empty cells. Your task is to remove knights until no knights\
that can attack one another with one move are left.
Always remove the knight who can attack the greatest number of knights. If there are two or more knights with the same\
number of attacks, remove the top-left one.
Example:
5
0K0K0
K000K
00K00
K000K
0K0K0
'''

size = int(input())
matrix = [list(input()) for _ in range(size)]

positions = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (2, 1),
    (2, -1),
    (1, 2),
    (1, -2)
)

removed_knights = 0

while True:
    max_attacks = 0
    knight_with_most_attacks_pos = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    knight_with_most_attacks_pos = [row, col]
                    max_attacks = attacks

    if knight_with_most_attacks_pos:
        r, c = knight_with_most_attacks_pos
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
