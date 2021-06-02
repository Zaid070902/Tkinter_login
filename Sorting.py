Numbers = [42, 12, 13, 89, 63, 11]

for y in range(0, 6):
    for x in range(0, 5):
        if Numbers[x] > Numbers[x + 1]:
            swap = Numbers[x]
            Numbers[x] = Numbers[x + 1]
            Numbers[x + 1] = Numbers[x]
            Numbers[x + 1] = swap

print(Numbers)
