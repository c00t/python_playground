number1 = input("Enter a number: ")
number1 = float(number1)
print(f"{number1} rounded to 2 decimal place is {round(number1, 2)}")
print(f"The absolute value of {number1} is {abs(number1)}")
number2 = input("Enter second number:")
number2 = float(number2)
print(f"The difference between {number1} and {number2} is an integer? {(number1-number2).is_integer()}")

