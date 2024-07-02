def capitalize_title(title):
  return title.title()

def check_sentence_ending(sentence):
  return sentence.endswith('.')

def clean_up_spacing(sentence):
  return sentence.strip()

def replace_word_choice(sentence, old_word, new_word):
  return sentence.replace(old_word, new_word)

capitalize_title("my hobbies")
check_sentence_ending("I like to hike, bake, and read.")
clean_up_spacing(" I like to go on hikes with my dog.  ")
print(replace_word_choice("I bake good cakes.", "good", "amazing"))