'''Alice is going to the mad tea party, to see her friends. On the way to the party, she needs to collect bags of tea.
You will be given an integer n for the size of the Wonderland territory with a square shape. On the following n lines,\
you will receive the rows of the territory:
•	Alice will be placed in a random position, marked with the letter "A".
•	On the territory, there will be bags of tea, represented as numbers. If Alice steps on a number position, she \
collects the tea bags and increases the quantity with the corresponding number.
•	There will always be one rabbit hole on the territory marked with the letter "R".
•	All of the empty positions will be marked with ".".
After the field state, you will be given commands for Alice's movements. Move commands can be: "up", "down", "left"\
or "right".
When Alice collects at least 10 bags of tea, she is ready to go to the tea party, and she does not need to continue\
collecting. Otherwise, if she steps on the rabbit hole or goes out of the territory, she can't return, and the program ends.
In the end, the path she walked had to be marked with '*'.
For more clarifications, see the examples below.
Example:
5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left
'''

size_matrix = int(input())

matrix = []
alice_pos = []
tea_bags = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size_matrix):
    matrix.append(input().split())

    if "A" in matrix[row]:
        alice_pos = [row, matrix[row].index("A")]
        matrix[row][alice_pos[1]] = "*"

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < size_matrix and 0 <= col < size_matrix):
        break

    alice_pos = [row, col]
    position = matrix[row][col]
    matrix[row][col] = "*"

    if position == "R":
        break

    if position.isdigit():
        tea_bags += int(position)

if tea_bags < 10:
    print("Alice didn't make it to the tea party.")

else:
    print("She did it! She went to the party.")

[print(*row) for row in matrix]
