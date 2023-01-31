'''Write a program that receives a matrix and prints the flattened version of it (a list with all the values).\
For example, the flattened list of the matrix: [[1, 2], [3, 4]] will be [1, 2, 3, 4].
On the first line, you will receive the number of a matrix's rows. On the next rows, you will get the elements for\
each column separated with a comma and a space ", ".
Example:
2
1, 2, 3
4, 5, 6
'''

matrix_row = int(input())
matrix1 = []
for elements in range(matrix_row):
    matrix = [int(s) for s in input().split(", ")]
    matrix1.extend(matrix)

print(matrix1)
