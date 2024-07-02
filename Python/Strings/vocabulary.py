def add_prefix_un(word):
  return 'un' + word 

def make_word_group(vocab_words):
  for string in vocab_words[1:]:
    vocab_words[vocab_words.index(string)] = vocab_words[0] + string
  return " :: ".join(vocab_words)

def remove_suffix_ness(word):
  vowels = 'aeiou'
  changed_word = word[:-4]
  if changed_word[-1] == 'i' and changed_word[-2] not in vowels:
    changed_word = changed_word[:-1] + 'y'
  return changed_word

def adjective_to_verb(sentence, index):
  word_list = sentence.split()
  adjective = word_list[index]
  for character in adjective:
    if character in '.?!':
      adjective = adjective.replace(character,'')
  return adjective + 'en'

print(add_prefix_un('wanted'))
print(make_word_group(['pre', 'serve', 'dispose', 'position']))
print(remove_suffix_ness('heaviness'))
print(adjective_to_verb('It got dark? as the sun set.', 2))