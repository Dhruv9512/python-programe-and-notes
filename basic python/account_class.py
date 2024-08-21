class Account:
    def __init__(self,balance,account_no):
        self.balance=balance
        self.account_no=account_no
    

    @property
    def dbt(self,value):
        self.value=value
    
    @dbt.setter
    def dbt(self,value):
        self.balance-=value

    def debit(self,value):
        self.dbt = value
    @property
    def crt(self,value):
        self.value=value


    @crt.setter
    def crt(self,value):
        self.balance+=value

    def credit(self,value):
        self.crt = value

   
    
    @property
    def print_balance(self):
        print(f"The balance of this {self.account_no} A/C:-  {self.balance}")


Arjuna = Account(20000,1256489658)  
Arjuna.credit(5000) 
Arjuna.print_balance

        