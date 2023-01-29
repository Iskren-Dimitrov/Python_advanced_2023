'''You will have to find all possible color combinations that can be used.
Write a program that finds colors in a string. You will be given a string on a single line containing substrings\
(separated by a single space) from which you will be able to form the following colors:
Main colors: "red", "yellow", "blue"
Secondary colors: "orange", "purple", "green"
To form a color, you should concatenate the first and the last substrings and check if you can get any of the above\
colors' names. If there is only one substring left, you should use it to do the same check.
You can only keep a secondary color if the two main colors needed for its creation could be formed from the given \
substrings:
•	orange = red + yellow
•	purple = red + blue
•	green = yellow + blue
Note: You could find some of the main colors needed to keep a secondary color after it is found.
When you form a color, remove both substrings. Otherwise, you should remove the last character of each substring and \
return them in the middle of the original string. If the string contains an odd number of substrings, you should put\
the substrings one position ahead.
For example, if you are given the string "re yellow bye" you could not form a color with the substring "re" and "bye",\
so you should remove the last character and return them in the middle of the string: "r by yellow".
In the end, print out the list with colors in the order in which they are found.
Example:
d yel blu e low redd
'''

from collections import deque

words = deque(input().split())

colors = {"red", "yellow", "blue", "orange", "purple", "green"}
needed_color = {"orange": {"red", "yellow"}, "purple": {"red", "blue"}, "green": {"yellow", "blue"}}

result = []

while words:
    first_word = words.popleft()
    second_word = words.pop() if words else ""

    for color in (first_word + second_word, second_word + first_word):
        if color in colors:
            result.append(color)
            break
    else:
        for element in (first_word[:-1], second_word[:-1]):
            if element:
                words.insert(len(words) // 2, element)

for color in set(needed_color.keys()).intersection(result):
    if not needed_color[color].issubset(result):
        result.remove(color)

print(result)
