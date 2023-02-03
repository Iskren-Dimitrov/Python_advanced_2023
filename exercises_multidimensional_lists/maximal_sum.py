from sys import maxsize

rows, columns = [int(s) for s in input().split()]
matrix = [[int(s) for s in input().split()] for s in range(rows)]

max_number = -maxsize

biggest_matrix = []

for row in range(rows - 2):
    for column in range(columns - 2):
        first_row = matrix[row][column:column + 3]
        second_row = matrix[row + 1][column:column + 3]
        third_row = matrix[row + 2][column:column + 3]

        current_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if current_sum > max_number:
            max_number = current_sum
            biggest_matrix = [first_row, second_row, third_row]

print(f"Sum = {max_number}")
[print(*biggest_matrix[s]) for s in range(len(biggest_matrix))]
