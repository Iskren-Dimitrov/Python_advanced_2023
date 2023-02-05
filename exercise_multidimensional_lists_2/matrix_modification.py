'''Write a program that reads a matrix from the console and changes its values. On the first line, you will get the\
matrix's rows - N. You will get elements for each column on the following N lines, separated with a single space. You \
will be receiving commands in the following format:
•	"Add {row} {col} {value}" – Increase the number at the given coordinates with the value.
•	"Subtract {row} {col} {value}" – Decrease the number at the given coordinates by the value.
If the coordinate is invalid, you should print "Invalid coordinates". A coordinate is valid if both of the given indexes\
are in range [0; len() – 1].
When you receive "END", you should print the matrix and stop the program.
Example:
3
1 2 3
4 5 6
7 8 9
Add 0 0 5
Subtract 1 1 2
END
'''

size_of_matrix = int(input())
matrix = [[int(s) for s in input().split()] for s in range(size_of_matrix)]

command = input()

while command != "END":
    command = command.split()
    type_command = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])

    if not (0 <= row < len(matrix) and 0 <= col < len(matrix)):
        print("Invalid coordinates")
    elif type_command == "Add":
        matrix[row][col] += value
    elif type_command == "Subtract":
        matrix[row][col] -= value

    command = input()

[print(*matrix[s]) for s in range(len(matrix))]
