'''First, you will be given two sequences of integers values on different lines. The values of the sequences are\
separated by a single space between them.
Keep in mind that each sequence should contain only unique values.
Next, you will receive a number - N. On the next N lines, you will receive one of the following commands:
•	"Add First {numbers, separated by a space}" - add the given numbers at the end of the first sequence of numbers.
•	"Add Second {numbers, separated by a space}" - add the given numbers at the end of the second sequence of numbers.
•	"Remove First {numbers, separated by a space}" - remove only the numbers contained in the first sequence.
•	"Remove Second {numbers, separated by a space}" - remove only the numbers contained in the second sequence.
•	"Check Subset" - check if any of the given sequences are a subset of the other. If it is, print "True". Otherwise,\
print "False".
In the end, print the final sequences, separated by a comma and a space ", ". The values in each sequence should be\
sorted in ascending order.
Example:
1 2 3 4 5
1 2 3
3
Add First 5 6
Remove Second 8 9 11
Check Subset
'''

first_sequences = set(int(s) for s in input().split())
second_sequences = set(int(s) for s in input().split())
command_number = int(input())

for commands in range(command_number):
    first_command, *data = input().split()

    command = first_command + " " + data.pop(0)

    if command == "Add First":
        [first_sequences.add(int(elements)) for elements in data]
    elif command == "Add Second":
        [second_sequences.add(int(elements)) for elements in data]
    elif command == "Remove First":
        [first_sequences.discard(int(elements)) for elements in data]
    elif command == "Remove Second":
        [second_sequences.discard(int(elements)) for elements in data]
    elif command == "Check Subset":
        if first_sequences.issubset(second_sequences) or second_sequences.issubset(first_sequences):
            print(True)
        else:
            print(False)

print(*sorted(first_sequences), sep=", ")
print(*sorted(second_sequences), sep=", ")
