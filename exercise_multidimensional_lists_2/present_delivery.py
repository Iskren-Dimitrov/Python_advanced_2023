'''The presents are ready, and Santa has to deliver them to the kids.
You will receive an integer m for the number of presents Santa has and an integer n for the size of the neighborhood\
with a square shape. On the following lines, you will receive the matrix, which represents the neighborhood.
Santa will be in a random cell, marked with the letter "S". Each cell stands for a house where children may live. If\
the cell has "X" on it, that means there lives a naughty kid. Otherwise, if a nice kid lives there, the cell is marked\
by "V". There can also be cells marked with "C" for cookies. All of the empty positions will be marked with "-".
Santa can move "up", "down", "left", "right" with one position each time. These will be the commands that you receive.\
If he moves to a house with a nice kid, the kid receives a present, but if Santa reaches a house with a naughty kid, he\
doesn't drop a present. If the command sends Santa to a cell marked with "C", Santa eats cookies and becomes happy and\
extra generous to all the kids around him* (meaning all of them will receive presents - it doesn't matter if naughty or\
nice). If Santa has been to a house, the cell becomes "-".
Note: *around him means on his left, right, upwards, and downwards by one cell. In this case, Santa doesn't move to\
these cells, or if he does, he returns to the cell where the cookie was.
If Santa runs out of presents or receives the command "Christmas morning", you should end the program.
Keep in mind that you should check whether all the nice kids received presents.
Example:
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning




'''


def eat_cookie(presents_left, nice_kids):
    for x, y in directions.values():
        r = santa_pos[0] + x
        c = santa_pos[1] + y

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                nice_kids += 1

            neighborhood[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

neighborhood = []
santa_pos = []

total_nice_kids = 0
nice_kids_visited = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(size):
    line = input().split()

    neighborhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][santa_pos[1]] = '-'

    total_nice_kids += line.count('V')

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == 'V':
        nice_kids_visited += 1
        presents -= 1
    elif house == 'C':
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or nice_kids_visited == total_nice_kids:
        break

    command = input()

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and nice_kids_visited < total_nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in neighborhood], sep='\n')
if nice_kids_visited == total_nice_kids:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')
