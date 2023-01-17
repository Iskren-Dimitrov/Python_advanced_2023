'''Write a program that reads a string with N integers from the console, separated by a single space, and reverses them\
using a stack. Print the reversed integers on one line, separated by a single space.
Example:
Input
1 2 3 4 5
'''

string_integers = [int(integers) for integers in input().split()]
reversed_stack = []

for numbers in range(len(string_integers)):
    reversed_stack.append(string_integers.pop())
reversed_stack_str = [str(integers) for integers in reversed_stack]
print(' '.join(reversed_stack_str))
