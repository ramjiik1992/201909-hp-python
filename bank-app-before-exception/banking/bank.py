#import accounts as a
#from banking.accounts import SavingsAccount,CurrentAccount,OverdraftAccount
from banking.accounts import *

class Bank:
    def __init__(self,name,interestRate):
        #super().__init__()
        self._name=name
        self._interestRate=interestRate
        
        #need to remember a list all the accounts that I have
        self._accounts={}
        self._account_count=0
        
    def _add_account(self,newAccount):
        self._account_count+=1
        accountNumber=self._account_count
        newAccount._set_account_number(accountNumber)
        self._accounts[accountNumber]=newAccount
        return accountNumber

    def open_savings_account(self,customerName,password,amount):
        newAccount=SavingsAccount(customerName,password,amount)
        return self._add_account(newAccount)

    def open_current_account(self,customerName,password,amount):
        newAccount=CurrentAccount(customerName,password,amount)
        return self._add_account(newAccount)
    
    def open_od_account(self,customerName,password,amount):
        newAccount=OverdraftAccount(customerName,password,amount)
        return self._add_account(newAccount)

    def _get_account(self,accountNumber):
        return self._accounts.get(accountNumber)
    
    def close_account(self,accountNumber,password):
            account=self._get_account(accountNumber)
            
            if account==None:return False
            
            if account.authenticate(password) and account.get_balance()>=0 :
                del self._accounts[accountNumber]
                return True
            else:
                return False
            
    def deposit(self,accountNumber,amount):
        account=self._get_account(accountNumber)
        if account==None :return False
        
        return account.deposit(amount)
        
    def withdraw(self,accountNumber,amount,password):
        account=self._get_account(accountNumber)
        if account==None :return False

        return account.withdraw(amount,password)
    
    def transfer(self,accountNumber,amount,password,targetAccount):
        src=self._get_account(accountNumber)
        if src==None : return False
        
        trgt=self._get_account(targetAccount)
        if trgt==None :return False
        
        if src.withdraw(amount,password):
            return trgt.deposit(amount)
        else:
            return False
        
    def get_account(self,accountNumber,password):
        account=self._get_account(accountNumber)
        if account.authenticate(password):
            return account
        else:
            return None
            
    def credit_interest(self):
        
        for account in self._accounts.values():
            account.credit_interest(self._interestRate)
            
    def print_list(self):
        for account in self._accounts.values():
            print('{}\t{}\t{}'.format(account.get_account_number(),account.get_balance(),account.get_name()))
            
        
