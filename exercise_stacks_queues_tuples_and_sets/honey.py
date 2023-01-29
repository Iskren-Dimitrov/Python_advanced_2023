'''We think the process of making honey is amazing! Let's learn more about how bees make honey.
Worker-bees collect nectar. When a worker-bee has found enough nectar, she returns to the hive to drop off the load and\
pass the nectar to waiting bees so they can really start the honey-making process.
You will receive 3 sequences:
•	a sequence of integers, representing working bees
•	a sequence of integers, representing nectar
•	a sequence of symbols – "+", "-", "*" or "/", representing the honey-making process.
Your task is to check if the bee has collected enough nectar to return to the hive and keep track of the total honey\
waiting bees made with the collected nectar.
Step one: check if a bee has collected enough nectar. You should take the first bee and try to match it with the last\
nectar:
•	If the nectar value is more or equal to the value of the bee, it is considered collected, and the bee returns to\
the hive to drop off the load (step two).
•	If the nectar value is less than the value of the bee, you should remove the nectar and try to match the bee with\
the next nectar's value until the bee collects enough nectar.
Step two: When a bee successfully collects nectar, she returns to the hive, and you should calculate the honey made.\
Take the first symbol in the sequence of symbols ("+", "-", "*" or "/") and make the corresponding calculation:
"{matched_bee} {symbol} {matched_nectar}"
The result represents the honey that is made from the passed nectar. The calculation should always return the absolute\
value of the result. After the calculation, remove the bee, the nectar, and the symbol.
Stop making honey when you are out of bees or nectar.
Example:
20 62 99 35 0 150
120 60 10 1 70 10
+ - + + / * - - /
'''

from collections import deque

bees = deque(int(s) for s in input().split())
nectar = deque(int(s) for s in input().split())
symbols = deque(input().split())

total_honey = 0

operations = {
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "-": lambda x, y: x - y,
    "+": lambda x, y: x + y,
}

while bees and nectar:
    current_bee = bees.popleft()
    current_nectar = nectar.pop()

    if current_nectar < current_bee:
        bees.appendleft(current_bee)
    elif current_nectar > current_bee:
        total_honey += abs(operations[symbols.popleft()](current_bee, current_nectar))

print(f"Total honey made: {total_honey}")

if bees:
    print(f"Bees left: {', '.join(str(s) for s in bees)}")

if nectar:
    print(f"Nectar left: {', '.join(str(s) for s in nectar)}")
