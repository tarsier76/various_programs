def darts(x, y):
  distance = (x ** 2 + y ** 2) ** 0.5

  if distance <= 1:
    return 10
  elif distance <= 5:
    return 5
  elif distance <= 10:
    return 1
  
  return 0
  
print(darts(2,2))