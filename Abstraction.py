from abc import ABC,abstractmethod 
class InvalidAmountException(Exception): 
    pass 
class BankAccount(ABC): 
     
    @abstractmethod 
    def deposit(self): 
        pass 
    @abstractmethod     
    def withdraw(self): 
        pass 
 
class AccountHolder(BankAccount): 
    def __init__(self,name,balance,amount): 
        self.amount=amount 
        self.name=name 
        self._balance=balance  
 
    def set_acc_number(self,acc_number): 
        self.__acc_number=acc_number  
    def get_acc_number(self): 
        return self.__acc_number     
 
    def deposit(self): 
        if self.amount<0: 
            raise InvalidAmountException  
        else: 
            print(f'After Deposit New Balance is:{self._balance+self.amount}')   
 
    def withdraw(self): 
        if self.amount<0: 
            raise InvalidAmountException  
        elif self.amount>self._balance: 
            raise ValueError 
                 
        else: 
            print(f'After Withdraw New Balance is:{self._balance-self.amount}')               
 
try: 
    obj = []
    for i in range(0, 5):  
        name = input("Enter Name: ")
        balance = int(input("Enter Balance: "))
        amount=int(input("Enter Amount: "))
        account = AccountHolder(name, balance,amount)
        obj.append(account)
        account.deposit()     
        account.withdraw()
           
except InvalidAmountException: 
    print("Invalid Amount") 
 
except ValueError: 
    print("Insufficient Balance for Withdraw")  
 
except : 
    print("Error Occured!")