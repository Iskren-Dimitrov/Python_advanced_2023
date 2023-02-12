'''Create a function called even_odd_filter() that can receive a different number of named arguments.\
The keys will be "even" and/or "odd", and the values will be a list of numbers.
When the key is "odd", you should extract only the odd numbers from its list. When the key is "even", you should\
extract only the even numbers from its list.
The function should return a dictionary sorted by the length of the lists in descending order. There will be no case\
of lists with the same length.
Submit only your function in the judge system.
Example:

print(even_odd_filter(

odd=[1, 2, 3, 4, 10, 5],

even=[3, 4, 5, 7, 10, 2, 5, 5, 2],

))
'''


def even_odd_filter(**kwargs):
    if "odd" in kwargs:
        kwargs["odd"] = [num for num in kwargs["odd"] if num % 2 != 0]

    if "even" in kwargs:
        kwargs["even"] = list(filter(lambda x: x % 2 == 0, kwargs["even"]))

    return dict(sorted(kwargs.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
