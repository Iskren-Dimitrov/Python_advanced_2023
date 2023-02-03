rows = int(input())
square_matrix = [[int(s) for s in input().split(", ")] for s in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for primary in range(rows):
    primary_diagonal.append(square_matrix[primary][primary])

for secondary in range(rows - 1, -1, - 1):
    secondary_diagonal.append(square_matrix[rows - 1 - secondary][secondary])

print(f"Primary diagonal: {', '.join([str(s) for s in primary_diagonal])}. Sum: {sum(primary_diagonal)}")
print(f"Secondary diagonal: {', '.join([str(s) for s in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
