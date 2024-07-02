
def check_number(num):
  numbers_sum = 0
  for i in str(num):
    numbers_sum += int(i) ** len(str(num))
  if numbers_sum == num:
    print(f"{num} is an Armstrong number.")
  else:
    print(f"{num} is NOT an Armstrong number.")

check_number(10)