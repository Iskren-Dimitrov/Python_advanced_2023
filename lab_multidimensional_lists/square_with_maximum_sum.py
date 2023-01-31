'''Write a program that reads a matrix from the console and finds the 2x2 top-left submatrix with biggest sum of its\
values.
On first line you will get matrix sizes in format "{rows}, {columns}".  On the next rows, you will get elements for\
each column, separated with a comma and a space ", ".
You should print the found submatrix and the sum of its elements, as shown in the examples.
Example:
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0	9 8
7 9
33
2, 4
10, 11, 12, 13
14, 15, 16, 17	12 13
16 17
58

'''


def read_matrix():
    data = input().split(', ')
    size = int(data[0])
    matrix = []

    for _ in range(size):
        row_data = list(map(int, input().split(', ')))
        matrix.append(row_data)

    return matrix


def submatrix_sum_func(matrix, row_index, column_index, matrix_size):
    total_sum = 0
    for row in range(row_index, row_index + matrix_size):
        for col in range(column_index, column_index + matrix_size):
            total_sum += matrix[row][col]

    return total_sum


def get_data_for_best_submatrix(matrix, size_of_submatrix):
    current_largest_row_index = 0
    current_largest_column_index = 0
    best_total_sum = submatrix_sum_func(matrix, 0, 0, size_of_submatrix)

    for row_index in range(len(matrix) - size_of_submatrix + 1):
        for col_index in range(len(matrix[row_index]) - size_of_submatrix + 1):
            current_sum = submatrix_sum_func(matrix, row_index, col_index, size_of_submatrix)

            if current_sum > best_total_sum:
                best_total_sum = current_sum
                current_largest_row_index = row_index
                current_largest_column_index = col_index

    return current_largest_row_index, current_largest_column_index


def print_function(submatrix_data, size):
    row_index, column_index = submatrix_data
    for row in range(row_index, row_index + size):
        data = []
        for col in range(column_index, column_index + size):
            data.append(matrix[row][col])
        print(' '.join(str(x) for x in data))
    print(submatrix_sum_func(matrix, row_index, column_index, size))


matrix = read_matrix()
size_of_submatrix = 2
submatrix_data = get_data_for_best_submatrix(matrix, size_of_submatrix)
print_function(submatrix_data, size_of_submatrix)
