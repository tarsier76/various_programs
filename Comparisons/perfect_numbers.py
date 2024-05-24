def check_number(num):
  aliquot_sum = sum([iter_num for iter_num in range(1, num) if num % iter_num == 0])
  
  if num <= 0:
    raise ValueError("Classification is only possible for positive integers.")

  if aliquot_sum == num:
    return 'Perfect'
  elif aliquot_sum < num:
    return 'Deficient'
  elif aliquot_sum > num:
    return 'Abundant'

print(check_number(1))