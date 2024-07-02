def test_membership(first_list, second_list):
  first_to_string = ''.join(str(num) for num in first_list)
  second_to_string = ''.join(str(num) for num in second_list)

  if first_list == second_list:
    return 'Lists are equal.'
  elif second_to_string in first_to_string:
    return 'First list contains second list.'
  elif first_to_string in second_to_string:
    return 'Second list contains first list.'
  return 'Lists are unequal.'
  
  
print(test_membership([1, 2, 3, 4, 5], [2, 3, 4]))
