'''Write a program that reads a number - N, representing the rows and columns of a square matrix. On the next N lines,\
you will receive rows of the matrix. Each row consists of ASCII characters. After that, you will receive a symbol.\
Find the first occurrence of that symbol in the matrix and print its position in the format: "({row}, {col})".\
You should start searching from the top left. If there is no such symbol, print the message "{symbol} does not occur\
in the matrix".
Example:
3
ABC
DEF
X!@
!
'''


def read_matrix_func():
    number_of_rows = int(input())
    current_matrix = []

    for row in range(number_of_rows):
        row_data = list(input())
        current_matrix.append(row_data)

    return current_matrix


def check_func_for_special_symbol(matrix, symbol):
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            current_element = matrix[row][col]
            if current_element == symbol:
                return row, col


def print_func(data, symbol):
    if data:
        print(data)
    else:
        print(f'{symbol} does not occur in the matrix')


matrix = read_matrix_func()
special_symbol = input()
print_func(check_func_for_special_symbol(matrix, special_symbol), special_symbol)
