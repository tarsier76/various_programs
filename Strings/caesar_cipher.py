def caesar_cipher(rotation, word):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  rot = int(rotation[3:])
  cipher_text_list = []
  
  for letter in word.lower():
    try:
      shift = (alphabet.index(letter) + rot) % 26 
    except ValueError:
      shift = 0
    if letter in alphabet:
      cipher_text_list.append(alphabet[shift]) 
    else:
      cipher_text_list.append(letter)
  return "".join(cipher_text_list)
      
print(caesar_cipher('ROT1', 'hello.'))
      


