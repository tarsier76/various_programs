def get_rounds(round_number):
  rounds = []
  for i in range(3):
    rounds.append(round_number + i)
  return rounds

def concatenate_rounds(rounds_1, rounds_2):
  return rounds_1 + rounds_2

def list_contains_round(rounds, round_number):
  if round_number in rounds:
    return True
  return False 

def card_average(hand):
  sum = 0
  for card in hand:
    sum += card 
  return sum / len(hand)

def approx_average_is_average(hand):
  average_first_last = (hand[0] + hand[-1]) / 2
  average = card_average(hand)
  middle_card = hand[len(hand) // 2]

  if average_first_last == average or average == middle_card:
    return True
  return False

def average_even_is_average_odd(hand):
  even_avearge = sum(hand[1::2]) / len(hand[1::2])
  odd_average = sum(hand[0::2]) / len(hand[0::2])
  average = card_average(hand)

  if even_avearge == odd_average == average:
    return True 
  return False 

def maybe_double_last(hand):
  if hand[-1] == 11:
    hand[-1] = 11 * 2
  return hand 

print(get_rounds(27))
print(concatenate_rounds([17, 18, 19], [35, 46]))
print(list_contains_round([27, 28, 29, 35, 36], 30))
print(card_average([5, 6, 7]))
print(approx_average_is_average([2, 3, 4, 8, 8]))
print(average_even_is_average_odd([1, 2, 3]))
print(maybe_double_last([5, 9, 11]))

