
class BankingException(Exception):
    def __init__(self,accountNumber=0,message='Banking Exception'):
        super(BankingException,self).__init__(message)
        self.errorMessage=message
        self.accountNumber=accountNumber


class InvalidAccountNumberException(BankingException):
    def __init__(self,accountNumber,message='Invalid Account Number'):
        super(InvalidAccountNumberException,self).__init__(accountNumber,message)


class InvalidCredentialsException(BankingException):
    def __init__(self,accountNumber,message='Invalid Credentials'):
        super(InvalidCredentialsException,self).__init__(accountNumber,message)


class InvalidUserDetailsException(BankingException):
    def __init__(self,accountNumber,message='Invalid User Details'):
        super(InvalidUserDetailsException,self).__init__(accountNumber,message)


class InvalidDenominationException(BankingException):
    def __init__(self,accountNumber,message='Invalid Denomination Requested'):
        super(InvalidDenominationException,self).__init__(accountNumber,message)


class InsufficientBalanceException(BankingException):
    def __init__(self,accountNumber,requestedAmount,maxAllowed,message='Invalid Credentials'):
        super(InsufficientBalanceException,self).__init__(accountNumber,message)
        self.maxAllowed=maxAllowed
        self.requested=requestedAmount
        



