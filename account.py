class Account:
    def __init__(self,number,pin,overdraft_limit):
        self.number = number
        self.__pin = pin
        self.__balance= 0
        self.overdraft_limit = overdraft_limit
        self.transactions = []
    
    def check_balance(self,pin):
        if pin==self.__pin:
            return self.__balance
        else:
            return "wrong pin"
        
    def deposit(self, amount):
        self.__balance += amount
        self.transactions.append(f"Deposit: {amount}")
    def withdraw(self, amount):
        if amount > self.__balance + self.overdraft_limit:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount
        self.transactions.append(f"Withdrawal: {amount}")
    def view_details(self):
        return {"Account Number": self.number, "Balance": self.__balance, "Overdraft Limit": self.overdraft_limit}
    def change_owner(self, new_owner):
        # Simulate changing ownership by updating the account details
        pass
    def generate_statement(self):
        return "\n".join(self.transactions)
    def freeze_account(self):
        # Freeze the account by preventing further transactions
        pass
    def unfreeze_account(self):
        # Unfreeze the account by allowing transactions again
        pass
    def calculate_interest(self, rate):
        interest = self.__balance * rate / 100
        self.deposit(interest)
        self.transactions.append(f"Interest: {interest}")
    def transfer_funds(self, target_account, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append(f"Transfer: {amount} to {target_account.number}")
        target_account.transactions.append(f"Transfer: {amount} from {self.number}")
# Example
account = Account(8753210,1234,5000)
#account.deposit(2000)
#account.withdraw(1500)
#print(account.view_details())
print(account.generate_statement())   