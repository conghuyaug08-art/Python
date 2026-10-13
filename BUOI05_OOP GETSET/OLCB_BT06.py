class BankAccount:
    def __init__(self, account_number="", owner="", balance=0):     
        self.__account_number = account_number 
        self.__owner = owner       
        if balance < 0:
            raise ValueError("So du ban dau phai lon hon 0!")
        self.__balance = balance
        self.__status = "Hoat dong"
        self.__history = []

    def get_balance(self):
        return self.__balance

    def get_status(self):
        return self

