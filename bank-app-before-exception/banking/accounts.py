class BankAccount:
        
    def __init__(self, name,password,amount):
       
        #self.__accountNumber=BankAccount._account_count
        self.__name=''
        self.set_name(name)
        self.__balance=amount
        self.__password=password
        self.__accountNumber=None # not yet assigned.
        
    
    def deposit(self, amount):
        if amount<=0 :
            return False
        else:
            self.__balance+=amount
            return True
    
    def withdraw(self,amount,password):
        if amount<=0:
            return False
        elif amount>self.__balance :
            return False
        elif not self.authenticate(password):
            return False
        else:
            self.__balance-=amount
            return True
            
            
            
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
            return False
        else:
            self.__name=newName
            return True
     
    
    def authenticate(self, challengePassword):
        if  self.__password != challengePassword:
            return False
        else:
            return True
    
    def change_password(self,oldPassword,newPassword):
        if self.authenticate(oldPassword):
            self.__password=newPassword
            return True
        else:
            return False
        
    def show(self):
        print('BankAccount[Id={},Name={},Balance={},InterestRate={}]' 
              . format( self.__accountNumber,self.__name,self.__balance,BankAccount._interestRate))



class SavingsAccount(BankAccount):
 
    def __init__(self,name,password,balance):
        BankAccount.__init__(self,name,password,balance)
        self._min_balance=5000
    
    def withdraw(self,amount,password):
        if amount> self.get_balance()-self._min_balance:
            return False
        else:
            return super().withdraw(amount,password)

class CurrentAccount(BankAccount):
     
    def __init__(self,name,password,balance):
        #super(CurrentAccount).__init__(name,password,balance)
        BankAccount.__init__(self,name,password,balance)

    def credit_interest(self,interestRate):
        pass


class OverdraftAccount(BankAccount):
     
    def __init__(self,name,password,balance):
        #super(OverdraftAccount).__init__(name,password,balance)
        BankAccount.__init__(self,name,password,balance)
        self._od_limit=balance/10
    
    def withdraw(self,amount,password):
        if amount<0 :return False
        if not self.authenticate(password):return False
        if amount> self.get_balance()+self._od_limit: return False

        newBalance=self.get_balance()-amount
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

    
