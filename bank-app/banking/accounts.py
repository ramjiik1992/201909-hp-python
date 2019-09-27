from banking.exceptions import *

class BankAccount:
        
    def __init__(self, name,password,amount):
       
        #self.__accountNumber=BankAccount._account_count
        self.__name=''
        self.set_name(name)
        self.__balance=amount
        self.__password=password
        self.__accountNumber=None # not yet assigned.
        
    def _validate_denomination(self,amount):
        if amount<=0:
            raise InvalidDenominationException(self.__accountNumber,'Negative Amount Not Allowed')

    
    def deposit(self, amount):
        self._validate_denomination(amount)
        self.__balance+=amount
    
    def get_max_withdrawable_amount(self):
        raise NotImplementedError('method should be implemented by derived class')

    def withdraw(self,amount,password):
        self.authenticate(password)
        self._validate_denomination(amount)        
        max=self.get_max_withdrawable_amount()
        if amount>max :
            raise InsufficientBalanceException(self.__accountNumber,amount,max)
        
        self.__balance-=amount
            
            
            
    # need to pass interest rate from Bank to BankAccount
    def credit_interest(self, interestRate):
        self.__balance+=self.__balance*interestRate/1200
    
    def get_balance(self):
        return self.__balance;
    
    
    # not a valid BankAccount operation
    #def set_balance(self,amount):
    #    self.__balance+=amount
    
    def get_account_number(self): return self.__accountNumber
    
    def _set_account_number(self,accountNumber) : self.__accountNumber=accountNumber
    
    def _set_balance(self,amount):
        self.__balance=amount

    def get_name(self):return self.__name
    
    def set_name(self,newName):
        '''
            Banking Norm dictates that the name on account should have first and last name
        '''
        if len(newName.split())<2:
            raise InvalidUserDetailsException(self.__accountNumber,'Name must include last name')
        self.__name=newName
     
    
    def authenticate(self, challengePassword):
        if  self.__password != challengePassword:
            raise InvalidCredentialsException(self.__accountNumber)
    
    def change_password(self,oldPassword,newPassword):
        self.authenticate(oldPassword)
        # we will not reach here if authenticate fails
        self.__password=newPassword
        
        
    def show(self):
        print('BankAccount[Id={},Name={},Balance={},InterestRate={}]' 
              . format( self.__accountNumber,self.__name,self.__balance,BankAccount._interestRate))



class SavingsAccount(BankAccount):
 
    def __init__(self,name,password,balance):
        BankAccount.__init__(self,name,password,balance)
        self._min_balance=5000

    def get_max_withdrawable_amount(self):
        return self.get_balance()-self._min_balance    

class CurrentAccount(BankAccount):
     
    def __init__(self,name,password,balance):
        #super(CurrentAccount).__init__(name,password,balance)
        BankAccount.__init__(self,name,password,balance)
    
    def get_max_withdrawable_amount(self):
        return self.get_balance()

    def credit_interest(self,interestRate):
        pass


class OverdraftAccount(BankAccount):
     
    def __init__(self,name,password,balance):
        #super(OverdraftAccount).__init__(name,password,balance)
        BankAccount.__init__(self,name,password,balance)
        self._od_limit=balance/10

    def get_max_withdrawable_amount(self):
        return self.get_balance()+self._od_limit
    
    def withdraw(self,amount,password):
       
        super().withdraw(amount,password)
        newBalance=self.get_balance()
        if newBalance<0 :
            charge= -newBalance/20 #5% of od
            newBalance-=charge
            self._set_balance(newBalance)
        
        return True

    def deposit(self,amount):
        super().deposit(self,amount)
        self._adjust_od_limit()

    def credit_interest(self,rate):
        super().credit_interest(rate)
        self._adjust_od_limit()

    def _adjust_od_limit(self):
        if self.get_balance()/10 >self._od_limit:
            self._od_limit=self.get_balance()/10

    
