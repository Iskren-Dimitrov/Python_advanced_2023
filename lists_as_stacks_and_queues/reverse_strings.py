""""Reverse Strings
Write program that:
•	Reads an input string
•	Reverses it using a stack
•	Prints the result back on the console
Examples
I Love Python	nohtyP evoL I
Stacks and Queues	seueuQ dna skcatS"""

text = list(input())
reversed_text_stack = []

while len(text) > 0:
    reversed_text_stack.append(text.pop())
print(''.join(reversed_text_stack))
