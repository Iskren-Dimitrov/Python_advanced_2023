'''Your task is to collect as many eggs as possible.
On the first line, you will be given a number representing the size of the field. On the following few lines, you will\
be given a field with:
•	One bunny - randomly placed in it and marked with the symbol "B"
•	Number of eggs placed at different positions of the field and traps marked with "X"
Your job is to determine the direction in which the bunny should go to collect the maximum number of eggs. The\
directions that should be considered as possible are up, down, left, and right. If you reach a trap while checking some of the directions, you should not consider the fields after the trap in this direction. For more clarifications, see the examples below.
Note: Consider ONLY the paths from which the bunny has collected 1 or more eggs.
Example:
5
1 3 7 9 11
X 5 4 X 63
7 3 21 95 1
B 1 73 4 9
9 2 33 2 0
'''

matrix_size = int(input())

matrix = []
bunny_position = []
best_path = []

best_direction = None
max_eggs = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(matrix_size):
    matrix.append(input().split())

    if "B" in matrix[row]:
        bunny_position = [row, matrix[row].index("B")]

for direction, positions in directions.items():
    row, col = [
        bunny_position[0] + positions[0],
        bunny_position[1] + positions[1],
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < matrix_size and 0 <= col < matrix_size:
        if matrix[row][col] == "X":
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += positions[0]
        col += positions[1]

    if collected_eggs >= max_eggs:
        max_eggs = collected_eggs
        best_direction = direction
        best_path = path

print(best_direction)
[print(s) for s in best_path]
print(max_eggs)
