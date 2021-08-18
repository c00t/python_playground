number = int(input("Please input a positive integer:"))
for i in range(1, number + 1):
    if (number % i) == 0:
        print(f"{i} is a factor of {number}")

while True:
    number = input("Please input a number:")
    try:
        number = int(number)
        print(number)
    except ValueError:
        print("Try again.")

