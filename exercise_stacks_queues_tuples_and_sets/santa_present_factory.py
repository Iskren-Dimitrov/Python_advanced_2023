'''This year Santa has decided to share his secret with you. Get ready to learn how his elves craft all the presents.
First, you will receive a sequence of integers representing the number of materials for crafting toys in one box. After\
that, you will be given another sequence of integers – their magic level.
Your task is to mix materials with magic so you can craft presents, listed in the table below with the exact magic level:
Example:
10 -5 20 15 -30 10
40 60 10 4 10 0
'''

from collections import deque

materials = deque(int(s) for s in input().split())
magic_levels = deque(int(s) for s in input().split())

crafted = []
presents = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

while materials and magic_levels:
    material = materials.pop() if magic_levels[0] or not materials[0] else 0
    magic_level = magic_levels.popleft() if material or not magic_levels[0] else 0

    if not magic_level:
        continue

    product = material * magic_level

    if presents.get(product):
        crafted.append(presents[product])
    elif product < 0:
        materials.append(material + magic_level)
    elif product > 0:
        materials.append(material + 15)

if {"Doll", "Wooden train"}.issubset(crafted) or {"Teddy bear", "Bicycle"}.issubset(crafted):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join([str(s) for s in materials][::-1])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(s) for s in magic_levels])}")

[print(f"{toy}: {crafted.count(toy)}") for toy in sorted(set(crafted))]
