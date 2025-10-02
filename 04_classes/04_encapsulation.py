# private variables

class Bank:
    def __init__(self, balance, name):
        self.__balance = balance
        self.name = name
        
    def set_balance(self, balance):
        self.__balance += balance
        # self.__balance = self.__balance + balance
        
    def get_balance(self):
        return self.__balance

b = Bank(10,"Tej") #create an instance of the class
# print(b.__balance) # private variables used through the object
print(b.name)
print(b.set_balance(5000))
print(b.get_balance())

        
        