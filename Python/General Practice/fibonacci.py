def fibonacci():
    first = 0 
    second = 1
    for num in range(18):
        
        new_num = first + second 
        first = second
        second = new_num
    return first, second
        
print(fibonacci())