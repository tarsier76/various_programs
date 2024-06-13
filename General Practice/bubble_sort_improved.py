arr = [7, 12, 9, 11, 3]

def bubble_sort(array):
    for iter in range(len(array) - 1):
        swapped = False 
        for index in range(len(array) - 1 - iter):
            if arr[index] > arr[index + 1]:
                arr[index], arr[index + 1] = arr[index + 1], arr[index]
                swapped = True 
        if not swapped:
            return array 
    return array

print(bubble_sort(arr))