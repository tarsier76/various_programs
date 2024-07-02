def is_pangram(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'

  letters_count = set([char for char in text.lower() if char in alphabet])
  return len(letters_count) == 26

print(is_pangram('Nymphs blitz quick vex dwarf jog'))

  