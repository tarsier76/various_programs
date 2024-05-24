def collatz_conjecture(num):
  if num <= 0 or num is not int:
    raise ValueError("Only positive integers are allowed")
  
  steps = 0 
  while num != 1:
    if num % 2 == 0:
      num = num / 2
      steps += 1
    elif num % 2 == 1:
      num = 3 * num + 1
      steps += 1
    
  return steps

print(collatz_conjecture(245))