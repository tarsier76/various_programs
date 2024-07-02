def exchange_usd_and_eur():
  exchange_rate = 1.07

  currency = input("Enter what currency you want to exchange:\n1 for USD\n2 for EUR\n")

  if currency not in ['1', '2']:
    print("Invalid choice enter, '1' or '2'.\n")
    return exchange_usd_and_eur()

  while True:
    try:
      amount = float(input("Enter the amount of currency you want to convert: "))
      if currency == '1':
        print(f'{amount} USD converted to {amount / exchange_rate:.2f} EUR')
      else:
        print(f'{amount} EUR converted to {amount * exchange_rate:.2f} USD')
      break
    except ValueError:
      print("Invalid amount, try again.")

def get_number_of_bills(amount, denomination):
  total_bills = amount / denomination
  print(int(total_bills))

def exchange_with_tax(amount, exchange_rate, tax):
  exchanged_currency = amount / ( exchange_rate + exchange_rate / tax)
  print(exchanged_currency)


