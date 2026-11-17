first = 0
second = 1
for count in range(1, 20 + 1, 1):
    print(second)
    nextNumber = first + second
    first = second
    second = nextNumber
