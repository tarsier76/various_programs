def paired_brackets(string):
  opened = '[{('
  closed = ']})'
  stack = []

  for val in string:
    if val in opened:
      stack.append(val)
    elif val in closed:
      if opened[closed.index(val)] != stack.pop():
        return False 
  return not stack
  
print(paired_brackets('[{()}]'))