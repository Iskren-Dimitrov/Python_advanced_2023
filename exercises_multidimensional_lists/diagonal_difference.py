size_of_square_matrix = int(input())
matrix = [[int(s) for s in input().split()] for s in range(size_of_square_matrix)]

primary_diagonal = []
secondary_diagonal = []

for primary in range(size_of_square_matrix):
    primary_diagonal.append(matrix[primary][primary])

for secondary in range(size_of_square_matrix - 1, -1, -1):
    secondary_diagonal.append(matrix[size_of_square_matrix - secondary - 1][secondary])

sum_primary = sum(primary_diagonal)
sum_secondary = sum(secondary_diagonal)

difference = abs(sum_primary - sum_secondary)
print(difference)