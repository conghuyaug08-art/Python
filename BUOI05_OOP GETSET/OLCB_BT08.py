class LibraryBook:
    def __init__(self, ma_sach, ten_sach, tac_gia, don_gia, so_luong_ton=0):
        if isinstance(ma_sach, str) and len(ma_sach) == 5 and ma_sach[0] == "S":
            self.__ma_sach = ma_sach
        else:
            print("Ma sach khong hop le!")
            self.__ma_sach = "S0000"

        if isinstance(ten_sach, str) and ten_sach.strip():
            self.__ten_sach = ten_sach
        else:
            print("Ten sach khong hop le!")
            self.__ten_sach = "Chua co ten"

        if isinstance(tac_gia, str) and tac_gia.strip():
            self.__tac_gia = tac_gia
        else:
            print("Ten tac gia khong hop le!")
            self.__tac_gia = "Chua co tac gia"

        self.__don_gia = 1.0
        self.don_gia = don_gia

        self.__so_luong_ton = 0
        self.so_luong_ton = so_luong_ton

    @property
    def don_gia(self):
        return self.__don_gia

    @don_gia.setter
    def don_gia(self, value):
        if isinstance(value, (int,float)) and value > 0:
            self.__don_gia = value
        else:
            print("Don gia phai lon hon 0!")

    @property
    def so_luong_ton(self):
        return self.__so_luong_ton

    @so_luong_ton.setter
    def so_luong_ton(self, value):
        if isinstance(value, int) and not isinstance(value, bool) and value >= 0:
            self.__so_luong_ton = value
        else:
            print("So luong ton phi lon hon 0!")
    
    def get_ten_sach(self):
        return self.__ten_sach

    def set_ten_sach(self, value):
        if isinstance(value, str) and value.strip():
            self.__ten_sach = value
        else:
            print("Ten sach khong duoc de trong!")

    def get_tac_gia(self):
       return self.__tac_gia
    
    def set_tac_gia(self, value):
        if isinstance(value, str) and value.strip():
            self.__tac_gia = value
        else:
            print("Ten tac gia khong duoc de trong!")

    def borrow_book(self, quantity):
        if isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("So luong muon phai la so nguyen duong!")
            return

        if self.__so_luong_ton >= quantity:
            self.__so_luong_ton -= quantity
            print("Muon sach thanh cong!")
        else:
            print("Khong du sacch trong kho!")

    def restock(self, quantity):
        if isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("So luong nhap phai la so nguyen duong!")
            return

        self.__so_luong_ton += quantity
        print("Nhap sach thanh cong!")

    def total_value(self):
        return self.__so_luong_ton * self.__don_gia

    def display(self):
        print("====== THONG TIN SACH =======")
        print(f"Ma sach: {self.__ma_sach}")
        print(f"Ten sach: {self.__ten_sach}")
        print(f"Tac gia: {self.__tac_gia}")
        print(f"Don gia: {self.__don_gia:,.2f} VND")
        print(f"So luong ton: {self.__so_luong_ton}")
        print(f"Tong gia tri ton kho: {self.total_value():,.2f} VND")
    
def main():
    book1 = LibraryBook("S0102", "Lap trinh Python", "Nguyen Van A", 85000, 10)
    book2 = LibraryBook("A1234", "", "Nguyen Van B", -500, 5)

    print("\n=== 1. THONG TIN SACH ===")
    book1.display()
    book2.display()

    print("\n=== 2. CAP NHAT DON GIA ===")
    book1.don_gia = 90000
    book1.display()

    print("\n=== 3. THU GAN SO LUONG AM ===")
    book1.so_luong_ton = -5
    print(f"So luong ton hien tai: {book1.so_luong_ton}")

    print("\n=== 4. MUON SACH ===")
    book1.borrow_book(3)
    book1.borrow_book(100)

    print("\n=== 5. NHAP THEM SACH ===")
    book1.restock(5)

    print("\n=== 6. TONG GIA TRI TON KHO ===")
    print(f"Tong gia tri: {book1.total_value():,.2f} VND")

    print("\n=== 7. THONG TIN SAU CUNG ===")
    book1.display()


if __name__ == "__main__":
    main()
