longest_set = set()
longest_count = int(input())

for longest in range(longest_count):
    first, second = [numbers.split(",") for numbers in input().split("-")]

    first_range = set(range(int(first[0]), int(first[1]) + 1))
    second_range = set(range(int(second[0]), int(second[1]) + 1))

    intersection = first_range.intersection(second_range)

    if len(longest_set) < len(intersection):
        longest_set = intersection

print(f"Longest intersection is [{', '.join(str(s) for s in longest_set)}] with length {len(longest_set)}")