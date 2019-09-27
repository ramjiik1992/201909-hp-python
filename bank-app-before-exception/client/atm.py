#from __future__ import input

from utils.input import read_int,read_str

class ATM:
    def __init__(self,bank):
        self._bank=bank
        
    def start(self):
        
        while True:
            id=read_int('account number?') 
            password=read_str('password?')
            
            self._id=id
            self._pass=password
        
            if id==0 and password=='@dmin' :
                self._admin_menu()
            elif id==0 and password=='shutdown':
                return
            else:
                self._menu()
        
    def _menu(self):
        
        
        while True:
            choice= int(input('1. deposit\t2.withdraw\t3.show\t4.transfer\t5.close\t0.exit ?'))

            if   choice==1: self._deposit()
            elif choice==2: self._withdraw()
            elif choice==3: self._show()
            elif choice==4: self._transfer()
            elif choice==5: self._close()
            elif choice==0: return
            else: print('invalid choice. retry')
                
    def _deposit(self):
        amount=read_int('amount? ')        
        if self._bank.deposit(self._id,amount):
            print('success')
        else:
            print('deposit failed')
        
    
    def _withdraw(self):
        amount=read_int('amount? ')        
        if self._bank.withdraw(self._id,amount,self._pass):
            print('success')
        else:
            print('failed')
    
    def _transfer(self):
        amount=read_int('amount? ')
        target=read_int('target account ?')
        if self._bank.transfer(self._id,amount,self._pass,target):
            print('success')
        else:
            print('failed')
    
    def _show(self):
        a=self._bank.get_account(self._id,self._pass)
        if a!=None:
            print('{}\t{}\t{}'.format(a.get_account_number(),a.get_balance(),a.get_name()))
        else:
            print('Invalid credentials')
    
    def _close(self):
        password=read_str('enter your password again?')
        if self._bank.close_account(self._id,password) :
            print('your account is closed. your money will be sent using draft')
        else:
            print('close failed')
    
    def _admin_menu(self):
         while True:
            choice= read_int('1. print list\t2.credit interest ?')

            if   choice==1: self._print_account_list()
            elif choice==2: self._credit_interest()
            elif choice==0: return
            else: print('invalid choice. retry')
                
                
    def _credit_interest(self):
        self._bank.credit_interest()
        print('interest credited')
    
    def _print_account_list(self):
        self._bank.print_list()
    
    

