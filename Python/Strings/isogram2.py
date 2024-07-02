def is_isogram(word):
  word.lower().replace(" ","").replace("-","")
  return len(word) == len(set(word))

print(is_isogram('isogram- '))