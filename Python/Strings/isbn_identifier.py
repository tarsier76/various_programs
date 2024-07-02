def is_valid(isbn):
  digits = [int(char) if char != 'X' else 10 for char in isbn if char != '-']

  multipliers = [value for value in range(10, 0, -1)]

  multiplied_numbers = [digits[index] * multipliers[index] for index in range(10)]   

  return sum(multiplied_numbers) % 11 == 0 and len(digits) == 10
  
print(is_valid('3-598-21507-X'))

  


