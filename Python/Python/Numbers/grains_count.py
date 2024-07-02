square = None

def grains_per_square(sqr):
  global square
  if 1 < sqr > 64 and sqr is not int:
    raise ValueError("Square must be between 1 and 64")
  
  square = sqr
  print(f"Total number of grains on the chessboard is: {2 ** 63 + 1}")

  if sqr == 1:
    return 1
  elif sqr == 2:
    return 2
  else:
    return 2 ** (sqr - 1)
  

print(f"There are {grains_per_square(13)} grains on square {square}.")