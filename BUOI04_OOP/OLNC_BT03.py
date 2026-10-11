
class LibraryBook:
    def __init__(self, book_id="", title="", author="", is_borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.is_borrowed = is_borrowed

    def display(self):
        status = "Da muon" if self.is_borrowed else "Trong"
        print(f"{self.book_id} | {self.title} | {self.author} | {status}")


class LibraryManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        for b in self.books:
            if b.book_id == book.book_id:
                print("Ma sach da ton tai!")
                return

        self.books.append(book)
        print("Them sach thanh cong!")

    def borrow_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.is_borrowed:
                    print("Sach da duoc muon!")
                else:
                    book.is_borrowed = True
                    print("Muon sach thanh cong!")
                return

        print("Khong tim thay sach!")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.is_borrowed:
                    print("Sach chua duoc muon!")
                else:
                    book.is_borrowed = False
                    print("Tra sach thanh cong!")
                return

        print("Khong tim thay sach!")

    def search_by_title(self, keyword):
        found = False

        for book in self.books:
            if keyword.lower() in book.title.lower():
                book.display()
                found = True

        if not found:
            print("Khong tim thay sach phu hop!")

    def display_books(self):
        if not self.books:
            print("Thu vien chua co sach!")
            return

        for book in self.books:
            book.display()


def main():
    library = LibraryManager()

    library.add_book(LibraryBook("S01", "Lap trinh Python", "Nguyen Van A"))
    library.add_book(LibraryBook("S02", "Lap trinh C#", "Tran Van B"))
    library.add_book(LibraryBook("S03", "Co so du lieu", "Le Van C"))

    while True:
        print("\n===== QUAN LY THU VIEN =====")
        print("1. Them sach")
        print("2. Muon sach")
        print("3. Tra sach")
        print("4. Tim sach theo ten")
        print("5. Hien thi danh sach sach")
        print("0. Thoat")

        choice = input("Nhap lua chon: ")

        if choice == "1":
            book_id = input("Nhap ma sach: ")
            title = input("Nhap ten sach: ")
            author = input("Nhap tac gia: ")

            library.add_book(LibraryBook(book_id, title, author))

        elif choice == "2":
            book_id = input("Nhap ma sach can muon: ")
            library.borrow_book(book_id)

        elif choice == "3":
            book_id = input("Nhap ma sach can tra: ")
            library.return_book(book_id)

        elif choice == "4":
            keyword = input("Nhap tu khoa ten sach: ")
            library.search_by_title(keyword)

        elif choice == "5":
            library.display_books()

        elif choice == "0":
            print("Ket thuc chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
