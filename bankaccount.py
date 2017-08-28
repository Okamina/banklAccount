"""BankAccount program:
Accepting deposits
Allowing withdraw
Showing the balance
Showing the details of the account.
Check a pin"""

pin_olga = 1245
pin_tomak = 1369
pin_bartek = 7531


class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return "%s's account balance: $%.2f" % (self.name, self.balance)
  def show_balance(self):
    print ("%s's account balance: $%.2f" % (self.name, self.balance))
  def deposit(self, amount): 
    if amount <= 0:
      print ("Error. You can not deposit zero or less dollars")
    else:
      print ("Deposit amount: $%.2f" % (amount))
      self.balance += amount
      self.show_balance()
  def withdraw(self, amount):
    if amount > self.balance:
      print ("You can not withdraw more than you have")
    else:
      print ("Payout amount: $%.2f" % (amount))
      self.balance -= amount
      self.show_balance()

def run_bank_app(cilent):
  my_account = BankAccount(cilent)
  
  exit = False
  while exit == False:
    choice_of_operation = input("Enter operation: \n1. Show Balance\n2. Deposit money\n3. Withdraw money\n0. Exit\n")
    if choice_of_operation == "1":
      my_account.show_balance()
      print()
    elif choice_of_operation == "2":
      print()
      amount = int(input("Enter amount: "))
      print()
      print ("previous " + (my_account.__repr__()))
      my_account.deposit(amount)
      print()
    elif choice_of_operation == "3":
      print()
      amount = int(input("Enter amount: "))
      print()
      print ("previous " + (my_account.__repr__()))
      my_account.withdraw(amount)
      print()
    elif choice_of_operation == "0":
      exit = True
    else:
      print ("Wrong option")

cilent =  input("Enter your name: ")
cilent = cilent.lower()
if cilent == "olga":
  pin_check = int(input("Enter your PIN: "))
  if pin_olga == pin_check:
    run_bank_app(cilent)
  else:
    print("Wrong PIN")
elif cilent == "tomek":
  pin_check = int(input("Enter your PIN: "))
  if pin_tomak == pin_check:
    run_bank_app(cilent)
  else:
    print("Wrong PIN")
elif cilent == "bartek":
  pin_check = int(input("Enter your PIN: "))
  if pin_bartek == pin_check:
    run_bank_app(cilent)
  else:
    print("Wrong PIN")
else:
  print ("Wrong cilent")

