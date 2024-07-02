from string import ascii_lowercase

ALPHABET = set(ascii_lowercase)

def is_pangram(text):
  return ALPHABET.issubset(text.lower())

print(is_pangram('The quick brown fox jumps over the lazy dog.'))
