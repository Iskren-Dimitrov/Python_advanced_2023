n_number, m_number = [int(s) for s in input().split()]

first_sets_of_elements = {int(input()) for first_set in range(n_number)}
second_sets_of_elements = {int(input()) for second_set in range(m_number)}

union_set = first_sets_of_elements.intersection(second_sets_of_elements)
print(*union_set, sep="\n")