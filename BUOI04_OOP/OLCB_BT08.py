class Book:
    demSach = 0

    def __init__(self, maSach="", tenSach="", tacGia=""):
        self.maSach = maSach
        self.tenSach = tenSach
        self.tacGia = tacGia
        Book.demSach += 1

    def HienThi(self):
        print("-" * 20)
        print("HIEN THI THONG TIN")
        print("-" * 20)
        print(f"Ma sach: {self.maSach}")
        print(f"Ten sach: {self.tenSach}")
        print(f"Tac gia: {self.tacGia}")

    @staticmethod
    def TongSoSach():
        print(f"Tong so sach: {Book.demSach}")


def main():
    b1 = Book("B001", "Lap trinh Python", "Nguyen Van A")
    b2 = Book("B002", "Lap trinh C#", "Tran Van B")
    b3 = Book("B003", "Co so du lieu", "Le Van C")

    print("THONG TIN SACH 1")
    b1.HienThi()

    print("\nTHONG TIN SACH 2")
    b2.HienThi()

    print("\nTHONG TIN SACH 3")
    b3.HienThi()

    print()
    Book.TongSoSach()


if __name__ == "__main__":
    main()