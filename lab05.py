def mnoz(a,b):
    return print("wynik:", a*b)
def main():
    mnoz(2,3)
if __name__ == '__main__':
    main()

# import unittest
#
# class BankAccount:
#     def __init__(self, balance):
#         self.balance = balance
#     def deposit(self,amount):
#         if amount <= 0:
#             raise ValueError('kwota musi byc wieksza niz 0')
#         self.balance += amount
#     def withdraw(self,amount):
#         if amount <= 0:
#             raise Exception('kwota musi byc wieksza niz 0')
#         self.balance -= amount
#     def get_balance(self):
#         return self.balance
#
# class TestAcc(unittest.TestCase):
#     def setUp(self):
#         self.account = BankAccount(250)
#     def test_deposit(self):
#         self.account.deposit(25)
#         self.assertEqual(self.account.balance, 275)
#     def test_withdraw(self):
#         self.account.withdraw(50)
#         self.assertEqual(self.account.get_balance(), 200)
#     def test_deposit_fail(self):
#         with self.assertRaises(ValueError):
#             self.account.deposit(0)
#
# if __name__ == '__main__':
#     unittest.main()
