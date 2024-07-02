arr = [7, 12, 9, 4, 11]

def array_lowest_value(array):
    lowest = float("inf")
    for num in array:
        if num < lowest:
            lowest = num 
    return lowest

print(array_lowest_value(arr))
