'''Write a program that receives a matrix of numbers and prints a new one only with the numbers that are even.\
Use nested comprehension for that problem.
On the first line, you will receive the rows of the matrix. On the next rows, you will get elements for each column\
separated with a comma and a space ", ".
Example:
2
1, 2, 3
4, 5, 6
'''

rows_of_the_matrix = int(input())
matrix = []
even = []
for row in range(rows_of_the_matrix):
    command = [int(s) for s in input().split(", ") if int(s) % 2 == 0]
    matrix.append(command)

print(matrix)
