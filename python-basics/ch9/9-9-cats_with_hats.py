cats = [False for i in range(100)]

for i in range(100): # walk 100 times
    for j in range(100):  # 100 cats
        if (j+1) % (i+1) == 0:
            cats[j] = not cats[j]

for i in range(100):
    if cats[i]:
        print(f"#{i+1}")

