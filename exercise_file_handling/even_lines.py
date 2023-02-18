'''Write a program that reads a text file and prints on the console its even lines. Line numbers start from 0.\
Before you print the result, replace {"-", ",", ".", "!", "?"} with "@" and reverse the order of the words.
Example:
-I was quick to judge him, but it
wasn't his fault.
-Is this some kind of joke?! Is it?
-Quick, hide here. It is safer
'''

symbols = ["-", ",", ".", "!", "?"]

with open("files_handling_txt/file.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for row in range(0, len(text), 2):

    for symbol in symbols:
        text[row] = text[row].replace(symbol, "@")

    print(*text[row].split()[::-1], sep=" ")
