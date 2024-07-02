def add_prefix_un(word):
  return 'un' + word

def make_word_group(vocab_words):
  return (' :: ' + vocab_words[0]).join(vocab_words)

def remove_suffix_ness(word):
  return word[:-4] if word[-5] != 'i' else word[:-5] + 'y'

def adjective_to_verb(sentence, index):
  return sentence.split()[index].strip(".?!") + 'en'

print(add_prefix_un('wanted'))
print(make_word_group(['pre', 'serve', 'dispose', 'position']))
print(remove_suffix_ness('heaviness'))
print(adjective_to_verb('It got dark? as the sun set.', 2))