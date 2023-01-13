"""You are given an algebraic expression with parentheses. Scan through the string and extract each set of parentheses.
Print the result back on the console.
Example:
1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"""

text = input()
parentheses_stack = []

for task in range(len(text)):
    if text[task] == "(":
        parentheses_stack.append(task)
    elif text[task] == ")":
        start_index = parentheses_stack.pop()
        print(text[start_index:task + 1])
