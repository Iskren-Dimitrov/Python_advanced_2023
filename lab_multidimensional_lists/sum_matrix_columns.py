'''Write a program that reads a matrix from the console and prints the sum for each column on separate lines.
On the first line, you will get matrix sizes in format "{rows}, {columns}". On the next rows, you will get elements for\
each column separated with a single space.
Example:
3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''

rows, columns = [int(s) for s in input().split(", ")]
matrix = []

for row in range(rows):
    current_command = [int(s) for s in input().split()]
    matrix.append(current_command)

for column_index in range(columns):
    sum = 0
    for row_index in range(rows):
        sum += matrix[row_index][column_index]
    print(sum)
