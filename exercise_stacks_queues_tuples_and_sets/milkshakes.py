'''You are learning how to make milkshakes.
First, you will be given two sequences of integers representing chocolates and cups of milk.
You have to start from the last chocolate and try to match it with the first cup of milk. If their values are equal,\
you should make a milkshake and remove both ingredients. Otherwise, you should move the cup of milk at the end of the\
sequence and decrease the value of the chocolate by 5 without moving it from its position.
If any of the values are equal to or below 0, you should remove them from the records right before mixing them with the\
other ingredient.
When you successfully prepare 5 chocolate milkshakes, or you have no more chocolate or cups of milk left, you need to\
stop making chocolate milkshakes.
Example:
20, 24, -5, 17, 22, 60, 26
26, 60, 22, 17, 24, 10, 55
'''

from collections import deque

chocolates = deque(int(s) for s in input().split(", "))
cups_of_milk = deque(int(s) for s in input().split(", "))

milkshakes = 0

while milkshakes != 5 and cups_of_milk and chocolates:
    chocolate = chocolates.pop()
    cup_of_milk = cups_of_milk.popleft()

    if chocolate <= 0 and cup_of_milk <= 0:
        continue
    elif chocolate <= 0:
        cups_of_milk.appendleft(cup_of_milk)
        continue
    elif cup_of_milk <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == cup_of_milk:
        milkshakes += 1
    else:
        cups_of_milk.append(cup_of_milk)
        chocolates.append(chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(str(s) for s in chocolates) or 'empty'}")
print(f"Milk: {', '.join(str(s) for s in cups_of_milk) or 'empty'}")
