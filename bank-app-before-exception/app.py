
import client.atm as atm
from banking.bank import Bank
import data.bankds as ds


icici = Bank('ICICI',12)

ds.add_dummy_accounts(icici)

icici_atm = atm.ATM(icici)

icici_atm.start()
    