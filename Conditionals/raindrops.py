def raindrops(num):
  sound = ''
  if num % 3 == 0:
    sound += 'Pling'
  if num % 5 == 0:
    sound += 'Plang'
  if num % 7 == 0:
    sound += 'Plong'
  
  return sound or str(num)

print(raindrops(105))