def encode(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  cipher = 'zyxwvutsrqponmlkjihgfedcba'
  encrypted_text = ''
  text_list = []

  for letter in text.lower():
    if letter in alphabet:
      encrypted_text += cipher[alphabet.index(letter)]
      if len(encrypted_text) % 5 == 0:
        text_list.append(encrypted_text)
        encrypted_text = ''
      elif len(encrypted_text) == len(text) and len(encrypted_text) < 5:
        return encrypted_text
  return " ".join(text_list)

print(encode('thequickbrownfoxjumpsoverthelazydog'))