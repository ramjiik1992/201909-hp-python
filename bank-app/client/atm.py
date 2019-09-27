#from __future__ import input

from utils.input import read_int,read_str,read_pass
from banking.accounts import *

class ATMException(Exception):
    pass

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
        
        try:
            while True:
                choice= int(input('1. deposit\t2.withdraw\t3.show\t4.transfer\t5.close\t0.exit ?'))

                if   choice==1: self._deposit()
                elif choice==2: self._withdraw()
                elif choice==3: self._show()
                elif choice==4: self._transfer()
                elif choice==5: self._close()
                elif choice==0: return
                else: print('invalid choice. retry')
        except InsufficientBalanceException as e:
            self._print_statement('Insufficient balance: Max withdrawal allowed is {}'.format(e.maxAllowed))
        except BankingException as be:
            self._print_statement(be)
        except ATMException as ae:
            return
                
    def _dispence_cash(self,amount):
        print('please collect your cash',amount)
    
    def _print_statement(self,message):
        print(message)
    
    def _deposit(self):
        amount=read_int('amount? ')        
        self._bank.deposit(self._id,amount)
        self._print_statement('success')
        
    
    def _withdraw(self):
        amount=read_int('amount? ')        
        if amount%100!=0:
            raise InvalidDenominationException(self._id,'Amount must be multiple of 100')
        self._bank.withdraw(self._id,amount,self._pass)
        self._dispence_cash(amount)
        self._print_statement('amount withdrawn {}'.format(amount))
    
    def _transfer(self):
        amount=read_int('amount? ')
        target=read_int('target account ?')
        self._bank.transfer(self._id,amount,self._pass,target)
        self._print_statement('transferred to {} :{}'.format(target,amount))
    
    def _show(self):
        a=self._bank.get_account(self._id,self._pass)
        if a!=None:
            print('{}\t{}\t{}'.format(a.get_account_number(),a.get_balance(),a.get_name()))
        else:
            print('Invalid credentials')
    
    def _close(self):
        password=read_str('enter your password again?')
        self._bank.close_account(self._id,password) 
        self._print_statement('your account is closed. your money will be sent using draft')
        raise ATMException()
    
    def _admin_menu(self):
         while True:
            choice= read_int('1. print list\t2.credit interest ?')

            if   choice==1: self._print_account_list()
            elif choice==2: self._credit_interest()
            elif choice==3: self._open_account()
            elif choice==0: return
            else: print('invalid choice. retry')
                
                
    def _credit_interest(self):
        self._bank.credit_interest()
        print('interest credited')
    
    def _print_account_list(self):
        self._bank.print_list()

    def _open_account(self):
        try:
            type=read_str('account type[savings,current,od]? ')
            name=read_str('name ?')
            password=read_pass('password');
            amount=read_int('amount?')

            self._bank.open_account(type,name,password,amount)
            print('account created')
        except:
            print('something went wrong')
            import traceback
            traceback.print_exc()
            


        

    
    

