class TransferError(Exception):
  pass

class BankAccount:
  def __init__(self, accountName, initialDeposit):
    self.name = accountName
    self.value = initialDeposit
    print(f"\nAccount {self.name} has been created.\nMoney: ${self.value}")

  def check_balance(self):
    print(f"\nCurrent balance for {self.name} is ${self.value:.2f}")

  def deposit(self, amount):
    self.value = self.value + amount
    print(f"\nDeposit succesful.")  
    self.check_balance()

  def check_transfer(self, amount):
    if self.value >= amount:
      return 
    else:
      raise TransferError('\nInsufficient funds in order to complete this process.')

  def withdraw(self, amount):
    try:
      self.check_transfer(amount)
      self.value = self.value - amount 
      print(f"\nAmount of ${amount} has been withdrawn.")
      self.check_balance()
    except TransferError as error:
      print(f'\nError occured: {error}')

  def transfer_money(self, amount, account):
    try:
      self.check_transfer(amount)
      self.withdraw(amount)
      account.deposit(amount)
      print("Transfer succeeded!")
    except TransferError as error:
      print(f"Transfer interrupted: {error}")

class InterestRewardsAcc(BankAccount):
  def deposit(self, amount):
    self.value = self.value + (amount * 1.05)
    print("Deposit complete.")
    self.check_balance()

class SavingsAcc(BankAccount):
  def __init__(self, accountName, initialDeposit):
    super().__init__(accountName, initialDeposit)
    self.fee = 5 

  def withdraw(self, amount):
    try:
      self.check_transfer(amount + self.fee)
      self.value = self.value - (amount + self.fee)
      print(f"Withdrawn ${amount + self.fee} from your savings account.")
      self.check_balance()
    except TransferError as error:
      print(f"Can't cover tax cost: {error}")

Dave = BankAccount("Dave", 500)
Sarah = BankAccount("Sarah", 2000)

Dave.withdraw(10)
Dave.withdraw(1000)
Sarah.deposit(1500)

Dave.transfer_money(100, Sarah)
Sarah.transfer_money(500, Dave)

Jim = InterestRewardsAcc("Jim", 1000)
Jim.deposit(200)

John = SavingsAcc("John", 5000)
John.withdraw(3000)