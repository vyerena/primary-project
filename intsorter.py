numbers = list(map(int, input().split(" ")))
print(numbers)
prod = 1
for i in numbers:
    prod *= i
print(prod)
