print(0)
print(1)
count = 2 

def fibonacci(first, second):
    global count
    while count < 19:
        new_num = first + second
        print(new_num)
        first = second
        second = new_num
        count += 1
        fibonacci(first, second)

fibonacci(0, 1)
