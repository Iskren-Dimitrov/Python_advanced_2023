""""Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following \
lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the\
command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
-	"{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in\
the dispenser for that person.
o	If there is enough water, print "{person_name} got water" and remove him/her from the queue.
o	Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the \
dispenser.
-	"refill {liters}" - add the given litters in the dispenser.
In the end, print how many liters of water have left in the format: "{left_liters} liters left".
Example:
2
Peter
Amy
Start
2
refill 1
1
End"""

from collections import deque


def add_names_in_deque():
    people_names = deque()
    names = input()
    while names != "Start":
        people_names.append(names)
        names = input()
    return people_names


water_litres = int(input())
people_deque = add_names_in_deque()
current_command = input()

while current_command != "End":
    if current_command.startswith("refill"):
        refill_commands_data = current_command.split()
        refill_water_amount = int(refill_commands_data[1])
        water_litres += refill_water_amount
    else:
        person = people_deque.popleft()
        current_litres = int(current_command)

        if current_litres <= water_litres:
            print(f'{person} got water')
            water_litres -= current_litres
        else:
            print(f'{person} must wait')
    current_command = input()

print(f"{water_litres} liters left")
