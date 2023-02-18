'''You are given a file called numbers.txt with the following content:
Example:
1
2
3
4
5
Create a program that reads the numbers from the file. Print on the console the sum of those numbers.
'''


def numbers_sum(file_name):
    data = open(file_name, 'r')
    sum_numbers = 0

    for number in data:
        sum_numbers += int(number)

    return sum_numbers


result = numbers_sum('text.txt')
print(result)
