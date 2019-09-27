#import accounts as a
#from banking.accounts import SavingsAccount,CurrentAccount,OverdraftAccount
from banking.accounts import *

class Bank:
    def __init__(self,name,interestRate):
        #super().__init__()
        self._name=name
        self._interestRate=interestRate
        self._account_types= {"savings":SavingsAccount,"current":CurrentAccount,"od":OverdraftAccount}
        
        #need to remember a list all the accounts that I have
        self._accounts={}
        self._account_count=0
        
    
    def _add_account(self,newAccount):
        self._account_count+=1
        accountNumber=self._account_count
        newAccount._set_account_number(accountNumber)
        self._accounts[accountNumber]=newAccount
        return accountNumber

    def open_account(self,acc_type,name,password,amount):
        _cls=self._account_types.get(acc_type)
        if _cls==None :
            raise BankingException('Invalid Account Type {}'.format(type))
        acc=_cls(name,password,amount)
        print('account created...')
        return self._add_account(acc)


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
        account = self._accounts.get(accountNumber)
        if(account==None):
            raise InvalidAccountNumberException(accountNumber)
        return account
    
    def close_account(self,accountNumber,password):
        account=self._get_account(accountNumber)
        account.authenticate(password)
        if  account.get_balance()<0 :
            raise InsufficientBalanceException(accountNumber,'Please repay OD Limit to close the account')
        del self._accounts[accountNumber]
            
    def deposit(self,accountNumber,amount):
        account=self._get_account(accountNumber)
        account.deposit(amount)
        
    def withdraw(self,accountNumber,amount,password):
        account=self._get_account(accountNumber)
        account.withdraw(amount,password)
    
    def transfer(self,accountNumber,amount,password,targetAccount):
        src=self._get_account(accountNumber)
        trgt=self._get_account(targetAccount)
        src.withdraw(amount,password)
        trgt.deposit(amount)
        
    def get_account(self,accountNumber,password):
        account=self._get_account(accountNumber)
        account.authenticate(password)
        return account
            
    def credit_interest(self):
       
        for account in self._accounts.values():
            account.credit_interest(self._interestRate)
            
    def print_list(self):
        for account in self._accounts.values():
            print('{}\t{}\t{}'.format(account.get_account_number(),account.get_balance(),account.get_name()))
            
        
