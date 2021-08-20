data = ((1, 2), (3, 4))
for i in range(0, len(data)):
    print(f"Row {i + 1} sum: {sum(data[i])}")

numbers = [4, 3, 2, 1]
print(numbers)
numbers2 = numbers[:]
print(numbers2)
numbers.sort()
print(numbers)