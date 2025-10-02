# private variables

class Bank:
    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name
        
    def set_balance(self, balance):
        self.__balance += balance
        self.__balance = self.__balance + balance
        
        
        
        
b = Bank(10,"Tej")
print(b.__balance)
print(b.name)
        
        