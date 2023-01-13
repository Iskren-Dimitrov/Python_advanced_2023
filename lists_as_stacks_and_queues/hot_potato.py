"""Hot Potato is a game in which children form a circle and toss a hot potato. The counting starts with the first kid.\
Every nth toss, the child holding the potato leaves the game. When a kid leaves the game, it passes the potato to the\
next kid. It continues until there is only one kid left.
Create a program that simulates the game of Hot Potato. On the first line, you will receive kids' names, separated by a\
single space. On the second line, you will receive the nth toss (integer) in which a child leaves the game.
Print every kid who is removed from the circle in the format "Removed {kid}". In the end, print the only kid left in\
the format "Last is {kid}".
Example:
George Peter Michael William Thomas
10"""



from collections import deque

kids_names = input().split()
count_kids = int(input())
counter = 0

kids = deque(kids_names)

while len(kids) > 1:
    counter += 1
    current_kid = kids.popleft()
    if counter == count_kids:
        print(f"Removed {current_kid}")
        counter = 0
    else:
        kids.append(current_kid)

print(f"Last is {''.join(kids)}")