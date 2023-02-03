rows, columns = [int(s) for s in input().split()]
start_end = ord("a")

for row in range(start_end, start_end + rows):
    for column in range(start_end, start_end + columns):
        print(f"{chr(row)}{chr(row + column - start_end)}{chr(row)}", end=' ')

    print()
