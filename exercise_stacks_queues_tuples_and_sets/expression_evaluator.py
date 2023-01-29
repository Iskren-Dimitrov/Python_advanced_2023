'''Write a program that evaluates a string expression. You will be given that string expression on the first line in\
the form of numbers and operators separated with a single space from each other. Your job is to take that string\
expression and calculate the result after evaluating it.
To do that, you have to follow a simple rule. If, for example, we have this string "2 4 * 1 3 -", the first time we\
meet an operator (*), we should take all the numbers we have so far (2, 4), apply that operation to them, and save the\
result (8). The next time we meet an operator (-), we again take all the numbers we have (8, 1, 3) and apply the\
operator to them in that order (8 - 1 - 3 = 4). In the end, we print the result.
All the numbers will always be integers, and the possible operators are "*", "+", "-", "/". It is important to keep the\
order of the numbers (especially for "/" and "-" because the order matters). When having a division, you should round the result to the lower integer.
Example:
6 3 - 2 1 * 5 /
'''

from functools import reduce
from math import floor

expressions = input().split()

index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: int(a) * int(b), expressions[:i]),
    "/": lambda i: reduce(lambda a, b: int(a) / int(b), expressions[:i]),
    "+": lambda i: reduce(lambda a, b: int(a) + int(b), expressions[:i]),
    "-": lambda i: reduce(lambda a, b: int(a) - int(b), expressions[:i]),
}

while index < len(expressions):
    element = expressions[index]

    if element in "*/+-":
        result = functions[element](index)
        [expressions.pop(1) for i in range(index)]
        expressions[0] = result
        index = 0

    index += 1

print(floor(int(expressions[0])))
