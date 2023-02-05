'''Write a program to flatten several lists of numbers received in the following format:
	String with numbers or empty strings separated by "|"
	Values are separated by spaces (" ", one or several)
	Order the output list from the last to the first matrix sub-lists and their values from left to right as shown below
Example:
1 2 3 |4 5 6 |  7  88
'''


numbers = input().split("|")
numbers_lst = []


for numbers in numbers[::-1]:
    numbers_lst.extend(numbers.split())

print(*numbers_lst)

#
# numbers = input().split("|")
# numbers_lst = []
# result = []
#
# for numbers in numbers[::-1]:
#     numbers_lst.append(numbers.split())
#
# for results in numbers_lst:
#     for number in results:
#         result.append(number)
#
# print(' '.join(result))