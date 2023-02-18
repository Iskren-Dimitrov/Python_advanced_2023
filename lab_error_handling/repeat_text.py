'''Write a program that receives a text on the first line and times (to repeat the text) that must be an integer.\
If the user passes a non-integer type for the times variable, handle the exception and print a message
"Variable times must be an integer".
Example:
Hello
Bye

'''

from io import StringIO
import sys

test_input = '''Hello
2
'''

sys.stdin = StringIO(test_input)


def repeat_text(text, number):
    return text * number


try:
    text = input()
    number = int(input())
    print(repeat_text(text, number))

except ValueError:
    print("Variable times must be an integer")
