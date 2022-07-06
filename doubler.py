number = int(input("Input number \n"))

double = number * 2

print(double)

while True:
    try:
        n = input("Input number \n")
        n = int(n)
        break
    except ValueError:
        print("Not a valid integer!")

