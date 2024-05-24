def rotate(text, key):
  plain = 'abcdefghijklmnopqrstuvwxyz'
  cipher = [plain[(index + key) % 26] for index in range(26)]
  print(cipher)

  plain += plain.upper()
  print(plain)
  cipher.extend([char.upper() for char in cipher])
  print(cipher)

  result = [cipher[plain.index(char)] if char in plain else char for char in text]
  return ''.join(result)

print(rotate('abc abc', 2))