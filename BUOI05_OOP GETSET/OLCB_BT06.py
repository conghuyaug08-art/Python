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
        return self.__status

    def deposit(self, amount):
        if amount <= 0:
            print("So tien gui phai lon hon 0!")
            return 

        if self.__status != "Hoat dong":
            print("Tai khoan dang bi khoa!")
            return

        self.__balance += amount
        self.__history.append(f"Gui tien: +{amount}")
        print("Gui tien thanh cong!")


    def withdraw(self, amount):
        if amount <= 0:
            print("So tien rut phai lon hon 0!")
            return

        if self.__status != "Hoat dong":
            print("Tai khoan dang bi khoa!")
            return

        if self.__balance < amount:
            print("So du khong du de rut!")
            return

        self.__balance -= amount
        self.__history.append(f"Rut tien: -{amount}" )
        print("Rut tien thanh cong!")

    def transfer(self, other, amount):
        if amount <= 0:
            print("So tien chuyen phai lon hon 0!")
            return

        if self.__status != "Hoat dong" or other.__status != "Hoat dong":
            print("Mot trong hai tai khoan dang bi khoa!")
            return

        if self.__balance < amount:
            print("Tai khoan khong du tien de chuyen!")
            return

        self.__balance -= amount

        other.__balance += amount

        self.__history.append(f"Gui tien: -{amount}")
        other.__history.append(f"Nhan tien: +{amount}")

        print("Chuyen tien thanh cong!")

    def lock_account(self):
        if self.__status == "Hoat dong":
            self.__status = "Khoa"
            print("Khoa tai khoan thanh cong!")
        else:
            print("Taai khoan da bi khoa!")

    def unlock_account(self):
        if self.__status == "Khoa":
            self.__status = "Hoat dong"
            print("Mo khoa tai khoan thanh cong!")
        else:
            print("Tai khoan dang hoat dong!")

    def show_history(self):
        if len(self.__history) == 0:
            print("Chua co lich su giao dich!")
            return
        print("======== LICH SU GIAO DICH ========")
        for ls in self.__history:
            print(ls)

    def display(self):
        print(f"{'So tai khoan':<20}{'Chu tai khoan':<20}{'So du':<20}{'Trang thai':<10}")
        print(f"{self.__account_number:<20}{self.__owner:<20}{self.__balance:<20,.2f}{self.__status:<10}")
        
def main():
    tk1 = BankAccount("TK001", "Nguyen Van A", 5000000)
    tk2 = BankAccount("TK002", "Nguyen Van B", 3000000)

    # Gui tien vao tk1
    tk1.deposit(300000)
    tk1.display()
    print("\n---------------------------------------")
    
    # Rut tien vao tk2
    tk2.withdraw(200000)
    tk2.display()
    print("\n---------------------------------------")

    # Chuyen tien tu tk1 sang tk2
    tk1.transfer(tk2, 550000)
    tk1.display()
    tk2.display()
    print("\n---------------------------------------")

    # Lock tk1
    tk1.lock_account()
    tk1.deposit(50000)
    print("\n---------------------------------------")

    # Hien thi lich su giao dich
    tk1.show_history()
    tk2.show_history()

    print("\n---------------------------------------")
    
     # Thu truy cap truc tiep vao so du
    try:
        print(tk1.__balance)
    except AttributeError:
        print("Khong the truy cap truc tiep vao __balance!")


if __name__ == "__main__":
    main()  
