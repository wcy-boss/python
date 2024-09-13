class BankAccount:
    
    def __init__(self, account_number, balance) -> None:
        # 账号名
        self._account_number = account_number
        # 余额
        self.__balance = balance
        
    def __str__(self) -> str:
        return "账号:{} 余额:{}".format(
            self._account_number, 
            self.__balance
        )
        
    def __pay_charge(self):
        # 交手续费
        self.__balance -= 5
        
    def deposit(self, amount): # 存款
        self.__balance += amount
        
    def withdraw(self, amount): # 取款
        if amount <= 0:
            print(f"金额异常：{amount}，取不了！")
            return
        
        if self.__balance < amount:
            print("余额不足，取不了！")
            return
        
        self.__balance -= amount
        self.__pay_charge()
        
account = BankAccount("123456", 1000)

account.deposit(200)
account.withdraw(300)

# account.__pay_charge() # 无法访问私有方法和属性 AttributeError: 'BankAccount' object has no attribute '__pay_charge'
print(account)