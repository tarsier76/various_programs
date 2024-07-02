def value_of_card(card):
  if card in 'JQK':
    return 10
  elif card == 'A':
    return 1
  return int(card)
  
def higher_card(card_one, card_two):
  first_card = value_of_card(card_one)
  second_card = value_of_card(card_two)

  if first_card > second_card:
    return first_card
  elif first_card < second_card:
    return second_card
  return (first_card, second_card)
  
def value_of_ace(card_one, card_two):
  first_card = value_of_card(card_one)
  second_card = value_of_card(card_two)

  if card_one == 'A' and card_two == 'A':
    return 1
  if first_card + second_card <= 10:
    return 11
  return 1

def is_blackjack(card_one, card_two):
  first_card = value_of_card(card_one)
  second_card = value_of_card(card_two)
  
  return (first_card == 10 and card_one == 'A') or (second_card == 10 and card_two == 'A')
  
def can_split_pairs(card_one, card_two):
  first_card = value_of_card(card_one)
  second_card = value_of_card(card_two)

  return first_card == second_card
  
def can_double_down(card_one, card_two):
  cards_sum = value_of_card(card_one) + value_of_card(card_two)

  return 9 <= cards_sum <= 11

print(can_split_pairs('A','A'))
print(value_of_ace('A','A'))
print(can_double_down('3', '8'))