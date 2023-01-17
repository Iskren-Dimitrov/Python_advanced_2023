'''You have a fast-food restaurant, and the food you are offering is previously prepared.
Write a program that checks if you have enough food to serve lunch to all your customers. You also want to know who the\
client with the biggest order for that day is.
First, you will be given the quantity of the food you have for the day (an integer number). Next, you will be given a\
sequence of integers (separated by a single space), each representing the quantity of food in each order. Keep the\
orders in a queue.
Find the biggest order and print it. Next, you will begin servicing your clients from the first one that came. Before\
each order, check if you have enough food left to complete it:
•	If you have, remove the order from the queue and reduce the quantity of food in the restaurant.
•	Otherwise, stop serving.
Input
•	On the first line, you will be given the quantity of your food - an integer in the range [0, 1000]
•	On the second line, you will receive a sequence of integers, representing each order, separated by a single space
Output
•	On the first line, print the quantity of the biggest order
•	On the second line:
o	If you succeeded in servicing all your clients, print: "Orders complete".
o	Otherwise, print: "Orders left: {order1} {order2} .... {orderN}".
Constraints
•	The input will always be valid
Example:
348
20 54 30 16 7 9
'''

from collections import deque

food_for_today = int(input())
food_for_each_order = deque(int(s) for s in input().split())

biggest_order = max(food_for_each_order)
print(biggest_order)

for food in food_for_each_order.copy():
    if food_for_today - food >= 0:
        food_for_each_order.popleft()
        food_for_today -= food
    else:
        print(f"Orders left: {' '.join([str(i) for i in food_for_each_order])}")
        break
else:
    print(f"Orders complete")
