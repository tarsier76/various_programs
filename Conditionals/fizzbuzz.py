def fizz_buzz(num):
  for i in range(1, num):
    if i % 3 == 0 and i % 5 == 0:
      print("FizBuzz!")
    elif i % 3 == 0:
      print("Fizz!")
    elif i % 5 == 0:
      print("Buzz!")
    else:
      print(i)

fizz_buzz(100)


