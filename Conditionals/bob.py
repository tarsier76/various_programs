def bob_responses(dialogue):
  speech = dialogue.strip()
  is_question = dialogue.endswith('?')
  is_uppercase = dialogue.isupper()

  if not speech:
    return "Fine. Be that way!"
  elif is_question and is_uppercase:
    return "Calm down, I know what I'm doing!"
  elif is_uppercase:
    return "Whoa, chill out!"
  elif is_question:
    return "Sure"
  else:
    return "Whatever"
  

print(bob_responses("Hello"))