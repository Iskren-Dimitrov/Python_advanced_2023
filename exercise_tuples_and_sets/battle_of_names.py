count_battle_of_names = int(input())

odd_set = set()
even_set = set()

for row in range(1, count_battle_of_names + 1):
    name = input()
    ascii_sum_name = sum(ord(s) for s in name) // row

    if ascii_sum_name % 2 == 0:
        even_set.add(ascii_sum_name)
    else:
        odd_set.add(ascii_sum_name)

if sum(odd_set) == sum(even_set):
    print(*odd_set.union(even_set), sep=", ")
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
