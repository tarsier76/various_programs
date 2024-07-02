arr = [64, 34, 25, 5, 22, 11, 90, 12]

def selection_sort(array):
    for iter in range(len(array) - 1):
        min_index = iter
        for index in range(iter + 1, len(array)):
            if array[index] < array[min_index]:
                min_index = index 
        lowest_value = array.pop(min_index)
        array.insert(iter, lowest_value)
    return array

print(selection_sort(arr)) 