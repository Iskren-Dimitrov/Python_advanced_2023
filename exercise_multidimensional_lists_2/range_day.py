'''You are participating in a Firearm course. It is a training day at the shooting range.
You will be given a matrix with 5 rows and 5 columns. It is a shotgun range represented as some symbols separated by a\
single space:
•	Your position is marked with the symbol "A"
•	Targets marked with symbol "x"
•	All of the empty positions will be marked with "."
After the field state, you will be given an integer representing the number of commands you will receive. The possible \
commands are:
•	"move {right/left/up/down} {steps}" – you should move in the given direction with the given steps. You can only \
move if the field you want to step on is marked with ".".
•	"shoot {right/left/up/down}" – you should shoot in the given direction (from your current position without moving).\
Beware that there might be targets that stand in the way of other targets, and you cannot reach them - you can shoot\
only the nearest target. When you have shot a target, the field becomes empty position (".").
Validate the positions since they can be outside the field.
Keep track of all the shot targets:
•	If at any point there are no targets left, end the program and print: "Training completed! All {count_targets}\
targets hit.".
•	If, after you perform all the commands, there are some targets left print: "Training not completed!\
{count_left_targets} targets left.".
Finally, print the index positions of the targets that you hit, as shown in the examples.
Example:
. . . . .
x . . . .
. A . . .
. . . x .
. x . . x
3
shoot down
move right 4
move left 1
'''


def move(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position

    if matrix_field[r][c] == "x":
        return my_position

    return [r, c]


def shoot(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if matrix_field[r][c] == "x":
            matrix_field[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


size = 5
matrix_field = []

targets = 0
targets_hit = 0
targets_hit_positions = []
my_position = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    matrix_field.append(input().split())

    if "A" in matrix_field[row]:
        my_position = [row, matrix_field[row].index("A")]
        matrix_field[row][my_position[1]] = "."

    if "x" in matrix_field[row]:
        targets += matrix_field[row].count("x")

for _ in range(int(input())):
    command_info = input().split()

    if command_info[0] == "move":
        my_position = move(command_info[1], int(command_info[2]))
    elif command_info[0] == "shoot":
        target_down_pos = shoot(command_info[1])

        if target_down_pos:
            targets_hit_positions.append(target_down_pos)
            targets_hit += 1

        if targets == targets_hit:
            print(f"Training completed! All {targets} targets hit.")
            break

if targets_hit < targets:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_positions, sep="\n")
