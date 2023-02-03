rows, columns = [int(s) for s in input().split()]
matrix = [[s for s in input().split()] for s in range(rows)]

equal_blocks = 0

for row in range(rows - 1):
    for column in range(columns - 1):
        symbol = matrix[row][column]

        if matrix[row][column + 1] == symbol and matrix[row + 1][column] == symbol and matrix[row + 1][column + 1] \
                == symbol:
            equal_blocks += 1

print(equal_blocks)
