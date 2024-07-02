def is_isogram(word):
  for char in list(word):
    if word.count(char) > 1 and char not in ' -':
      return False
  return True

print(is_isogram('isogram- '))