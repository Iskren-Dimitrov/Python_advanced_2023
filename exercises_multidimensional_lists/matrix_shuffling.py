def check_valid_index(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], indexes[3]}.issubset(valid_columns):
        return True
    return False


def swap_command(command, indexes):
    if check_valid_index(indexes) and command == "swap" and len(indexes) == 4:
        row1, col1, row2, col2 = indexes

        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]                   

        print(*[' '.join(matrix[r]) for r in range(rows)], sep="\n")
    else:
        print("Invalid input!")


rows, columns = [int(s) for s in input().split()]
matrix = [input().split() for s in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command_type, *info = [int(s) if s.isdigit() else s for s in input().split()]

    if command_type == "END":
        break

    swap_command(command_type, info)
