try:
    n = int(input("Height: "))
except ValueError:
    n = int(input("Height: "))

while n < 1 or n > 8:
    n = int(input("Height: "))
for i in range(n):
    for j in range(n - 1 - i):
        print("", end=' ')
    for k in range(i + 1):
        print("#", end='')
    print()