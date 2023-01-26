text = input()
symbols_set = {}

for letter in text:
    if letter not in symbols_set.keys():
        symbols_set[letter] = 0
    symbols_set[letter] += 1

for symbol, number in sorted(symbols_set.items()):
    print(f"{symbol}: {number} time/s")
