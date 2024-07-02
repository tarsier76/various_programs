def check_triangle(a, b, c):
  if a == 0 or b == 0 or c == 0:
    return "A triangle cannot have a side equal to 0."
  elif a + b >= c and b + c >= a and a + c >= b:
    if a == b == c:
      return "Equilateral triangle."
    elif a == b or b == c or c == a:
      return "Isosceles triangle."
    else:
      return "Scalene triangle."
  else:
    return "Not viable triangle."

print(check_triangle(5, 6, 7))

