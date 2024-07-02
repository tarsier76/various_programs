def answer(question):
  

  if 'what is' in question.lower() and question.split()[2].isnumeric():
    string_to_list = question.strip('What is ?').replace('plus','+').replace('minus','-').replace('multiplied by','*').replace('divided by','/').split()   
    
    for x in range(0, len(string_to_list), 2):
      if not string_to_list[x].isnumeric():
        raise ValueError("Syntax error, bad operation.")

    return eval(''.join(string_to_list))

  else:
    raise ValueError("Unknown operation.")


print(answer('What is 5 plus 1 multiplied by 10 minus 10?'))