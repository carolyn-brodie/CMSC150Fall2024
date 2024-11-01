out = list(range(1,100,2)) + list(range(97, 0, -2))
# print(out)

out2 = []
for number in range(1,100):
    if number % 2 == 1:
        out2.append(number)
for number in range(97, 0, -1):
    if number % 2 == 1:
        out2.append(number)

print(out2)
