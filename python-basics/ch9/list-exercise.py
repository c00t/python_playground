food = ["rice", "beans"]
food.append("broccoli")
food.extend(("bread", "pizza"))
print(food[0:2])
print(food[-1])
breakfast = "eggs, fruit, orange juice".split(", ")
print(f"length of breakfast is 3? {len(breakfast) == 3}")
lengths = [len(value) for value in breakfast]
print(lengths)