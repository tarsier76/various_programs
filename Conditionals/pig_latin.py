def language_change(word):
  vowels = ['a', 'e', 'i', 'o', 'u', 'y']
  if word[0] in vowels or word[:2] in ['xr', 'yt']:
    return word + 'ay'

  consonants = ''
  for letter in word:
    if letter not in vowels:
      consonants += letter
    else:
      break

  if consonants[0] + 'qu' in word:
    return word.replace(consonants[0] + 'qu','') + consonants[0] + 'qu' + 'ay'
  elif consonants + 'y' in word:
    return word.replace(consonants,'') + consonants + 'ay'
  elif consonants in word:
    return word.replace(consonants,'') + consonants + 'ay'
  

def translate(text):
  return ' '.join([language_change(word) for word in text.split()])

print(translate("my square rhythm chair"))