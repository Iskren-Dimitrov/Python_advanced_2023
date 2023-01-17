'''You have an empty stack. You will receive an integer – N. On the next N lines, you will receive queries. Each query is \
one of these four types:
•	'1 {number}' – push the number (integer) into the stack
•	'2' – delete the number at the top of the stack
•	'3' – print the maximum number in the stack
•	'4' – print the minimum number in the stack
It is guaranteed that each query is valid.
After you go through all the queries, print the stack from top to bottom in the following format:
"{n}, {n1}, {n2}, ... {nn}"
Example:
Input
9
1 97
2
1 20
2
1 26
1 20
3
1 91
4
'''

from collections import deque

integer_count = int(input())
stack_queries = deque()

for numbers in range(integer_count):
    current_command = input()

    if current_command.startswith("1 "):
        current_command = current_command.split()
        number = int(current_command[1])
        stack_queries.append(number)
    elif current_command == "2":
        if stack_queries:
            stack_queries.pop()
    elif current_command == "3":
        if stack_queries:
            print(max(stack_queries))
    elif current_command == "4":
        if stack_queries:
            print(min(stack_queries))

stack_queries.reverse()

print(*stack_queries, sep=", ")
