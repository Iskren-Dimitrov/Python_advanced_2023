'''You will receive a sequence of numbers (integers) separated by a single space. Separate the negative numbers from\
the positive. Find the total sum of the negatives and positives, and print the following:
On the first line, print the sum of the negatives
On the second line, print the sum of the positives
On the third line:
If the absolute negative number is larger than the positive number: "The negatives are stronger than the positives"
If the positive number is larger than the absolute negative number: "The positives are stronger than the negatives"
Note: you will not receive any zeroes in the input.
Example:
1 2 -3 -4 65 -98 12 57 -84
'''


def positive_numbers(positive):
    sum_positive = 0
    for number in positive:
        if number > 0:
            sum_positive += number
    return sum_positive


def negative_numbers(negative):
    sum_negative = 0
    for number in negative:
        if number < 0:
            sum_negative += number
    return sum_negative


def print_function(positive, negative):
    print(negative)
    print(positive)

    if abs(negative) > positive:
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(s) for s in input().split()]
positive = positive_numbers(numbers)
negative = negative_numbers(numbers)
print_function(positive, negative)
