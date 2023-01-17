'''You will be given a sequence consisting of parentheses. Your job is to determine whether the expression is balanced.\
A sequence of parentheses is balanced if every opening parenthesis has a corresponding closing parenthesis that occurs\
after the former. There will be no interval symbols between the parentheses. You will be given three types of\
parentheses: (), {}, and [].
{[()]} - Parentheses are balanced.
(){}[] - Parentheses are balanced.
{[(])} - Parentheses are NOT balanced.
Input
•	On a single line, you will receive a sequence of parentheses.
Output
•	For each test case, print on a new line "YES" if the parentheses are balanced.
•	Otherwise, print "NO"
Constraints
•	1 ≤ lens ≤ 1000, where the lens is the length of the sequence
•	Each character of the sequence will be one of {, }, (, ), [, ]
Example:
{[()]}
'''

from collections import deque

parentheses = input()

symbols = deque(parentheses)
parentheses_stack = deque()

while symbols:
    left_parentheses = symbols.popleft()
    if left_parentheses in "([{":
        parentheses_stack.append(left_parentheses)
    elif not parentheses_stack:
        print("NO")
        break
    else:
        if f"{parentheses_stack.pop() + left_parentheses}" not in "{}[]()":
            print("NO")
            break
else:
    print("YES")
