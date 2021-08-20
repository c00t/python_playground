universities = [
    # the name of university, the total number of enrolled students, the annual tuition fees
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]


def enrollment_stats(item):
    return ([item[i][1] for i in range(0, len(item))],
            [item[i][2] for i in range(0, len(item))])


def mean(item):
    return sum(item)/len(item)


# def median(item): # 传递进函数中时，是shallow copy，还是deep copy？估计是浅复制,验证过了，传入的是引用
#     new_item = item[:]
#     new_item.sort()
#     index = round(len(new_item) / 2 - 1.0 + 0.1) # some trick here
#     return new_item[index]

def median(values):
    """Return the median value of the list `values`"""
    values.sort()
    # If the number of valus is odd,
    # return the middle value of the list
    if len(values) % 2 == 1:
        # The value at the center of the list is the value
        # at whose index is half of the length of the list,
        # rounded down
        center_index = int(len(values) / 2)
        return values[center_index]
    # Otherwise, if the length of the list is even, return
    # the mean of the two center values
    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) + 1) // 2
        return mean([values[left_center_index], values[right_center_index]])


students, fees = enrollment_stats(universities)
print(fees)
print(f"Total students: {sum(students):,}")
print(f"Total tuition: $ {sum(fees):,}")
print("\n")
print(f"Student mean: {mean(students):,.2f}")
print(f"Student median: {median(students):,}")
print("\n")
print(f"Tuition mean: $ {mean(fees):,.2f}")
print(f"Tuition median: $ {median(fees):,}")
print(fees)