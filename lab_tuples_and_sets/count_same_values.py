'''You will be given numbers separated by a space. Write a program that prints the number of occurrences of each number\
in the format "{number} - {count} times". The number must be formatted to the first decimal point.
Example:
-2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
'''

numbers = tuple([float(s) for s in input().split()])
dictionary_numbers = {}

for number in numbers:
    if number not in dictionary_numbers.keys():
        dictionary_numbers[number] = 0
    dictionary_numbers[number] += 1

for number, count in dictionary_numbers.items():
    print(f"{number} - {count} times")
