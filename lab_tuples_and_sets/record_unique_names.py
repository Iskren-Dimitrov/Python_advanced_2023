'''Write a program, which will take a list of names and print only the unique names in the list.
The order in which we print the result does not matter.
Example:
8
Lee
Joey
Lee
Joe
Alan
Alan
Peter
Joey
'''

count_names = int(input())

unique_names = set()

for count_name in range(count_names):
    names = input()
    unique_names.add(names)
print('\n'.join(unique_names))
