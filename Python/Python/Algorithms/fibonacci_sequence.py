def fib(n):
    current = 0
    parent = 1 
    grandparent = 0 
    if n == grandparent:
        return grandparent
    elif n == parent:
        return parent
    for num in range(n - 1):
        current = parent + grandparent
        parent, grandparent = current, parent
    return current
        