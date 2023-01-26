count_chemical_elements = int(input())
chemical_elements_set = set()

for elements in range(count_chemical_elements):
    current_elements = input()
    for element in current_elements.split():
        chemical_elements_set.add(element)

print(*chemical_elements_set, sep="\n")