def draw(letter):
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  iteration = 2
  empty_spaces_list = []
  diamond = []

  for value in alphabet:
    if alphabet.index(value) == alphabet.index(letter) + 1:
      break
    
    elif value == 'A':
      empty_spaces_list.append(['A'])
    else:
      empty_spaces_list.append([' ' if 1 <= times < (alphabet.index(value) + iteration - 1) else value for times in range((alphabet.index(value) + iteration))])
      iteration += 1

  values_with_spaces = empty_spaces_list + empty_spaces_list[:-1][::-1]
  
  for sublist in values_with_spaces:
    if letter in sublist:
      continue 
    else:
      spaces_difference = (len(empty_spaces_list[-1]) - len(sublist)) / 2
      for prepending in range((int(spaces_difference))):
        sublist.insert(0, ' ')
        sublist.append(' ')

  for sublist in values_with_spaces:
    string = ''.join(sublist)
    diamond.append(string)

  return '\n'.join(line for line in diamond)


print(draw('F'))

    