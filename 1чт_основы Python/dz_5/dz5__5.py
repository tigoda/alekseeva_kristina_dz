import collections

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
unique_number = set()
repeated_number = set()
c = collections.Counter()
for number in src:
    c[number] += 1
    if number in repeated_number:
        continue
    if number in unique_number:
        unique_number.discard(number)
        repeated_number.add(number)
        continue
    unique_number.add(number)
print([number for number in src if number in unique_number])
print(c)
