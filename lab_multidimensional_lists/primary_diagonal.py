'''Write a program that finds the sum of all numbers in a matrix's primary diagonal (runs from top left to bottom \
right). On the first line, you will receive an integer N – the size of a square matrix. The next N lines holds the\
values for each column - N numbers, separated by a single space.
Example:
3
11 2 4
4 5 6
10 8 -12
'''

size = int(input())
matrix = [[0] * size for row in range(0, size)]

for x in range(0, size):
    line = list(map(int, input().split()))
    for y in range(0, size):
        matrix[x][y] = line[y]

sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))
print(sum_diagonal)
