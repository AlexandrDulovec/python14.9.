n = int(input("Vložte číslo: "))
for i in range(n, 0, -1):
    for j in range(1, i + 1):
        if i % 2 == 0:
            print(i - j + 1, end='')
        else:
            print(j, end='')
    print()
