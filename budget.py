class Budget:

    def __init__(self, category, amount): 
        self.category = category
        self.amount = amount
        #self.balance = balance
        #self.transfer = transfer


    def deposit(self):
        print(".....You are about to make a deposit..... \n")
       depst =  int(print("How much would you like to deposit \n"))
        return "Deposit operation"

    def withdraw_op(self):
        print("Withdraw from your account? \n")
        wthdrw = int(print("Specify withdrawal amount \n"))
        pass

    def acct_balance(self):
        print("Account balance details")
        pass
    
    def transfer(self):
        print("Your are about to make a TRANSFER to another account \n")
        pass

clothing = Budget("clothing", 1000)
food = Budget("food", 2500)
entertainment = Budget("entertainment", 1500)

print(clothing.deposit())
print(food.deposit())
print(entertainment.deposit())

print(clothing.withdraw_op())
print(food.withdraw_op())
print(entertainment.withdraw_op())

print(clothing.transfer())
print(food.transfer())
print(entertainment.transfer())