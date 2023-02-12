'''Create a function called even_odd() that can receive a different quantity of numbers and a command at the end.\
The command can be "even" or "odd". Filter the numbers depending on the command and return them in a list.\
Submit only the function in the judge system.
Submit only your function in the judge system.
Example:
print(even_odd(1, 2, 3, 4, 5, 6, "even"))
'''


def even_odd(*args):
    result = []
    command = args[-1]
    for numbers in args[:-1]:
        if command == "even":
            if numbers % 2 == 0:
                result.append(numbers)
        elif command == "odd":
            if numbers % 2 != 0:
                result.append(numbers)
    return result


print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
