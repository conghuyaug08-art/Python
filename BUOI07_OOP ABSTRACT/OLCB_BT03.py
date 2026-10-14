from abc import ABC, abstractmethod
class Student:
    def __init__(self, ma_sv, ho_ten):
        self.ma_sv = ma_sv
        self.ho_ten = ho_ten

class AbstractStudentManager(ABC):
    @abstractmethod
    def add_student(self, student):
        pass

    @abstractmethod
    def remove_student(self, ma_sv):
        pass

    @abstractmethod
    def update_student(self, ma_sv, new_name):
        pass

    @abstractmethod
    def display_all(self):
        pass

class StudentManager(AbstractStudentManager):
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
        print("Them thanh cong!")

    def remove_student(self, ma_sv):
        for sv in self.students:
            if sv.ma_sv == ma_sv:
                self.students.remove(sv)
                print("Xoa thanh cong!")
                return
        print("Khong tim thay sinh vien!")
        return None

    def update_student(self, ma_sv, new_name):
        for sv in self.students:
            if sv.ma_sv == ma_sv:
                sv.ho_ten = new_name
                print("Cap nhat thanh cong!")
                return 
        print("Khong timm thay sinh vien!")
        return None

    def display_all(self):
        if not self.students:
            print("Danh sach rong!")
            return
        for sv in self.students:
            print(f"Ma sinh vien: {sv.ma_sv}")
            print(f"Ho ten: {sv.ho_ten}")


def main():
    manager = StudentManager()

    while True:
        print("\n===== QUAN LY SINH VIEN =====")
        print("1. Them sinh vien")
        print("2. Xoa sinh vien")
        print("3. Sua ho ten sinh vien")
        print("4. Hien thi danh sach")
        print("5. Thoat")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            ma_sv = input("Nhap ma sinh vien: ")
            ho_ten = input("Nhap ho ten: ")

            sv = Student(ma_sv, ho_ten)
            manager.add_student(sv)

        elif chon == "2":
            ma_sv = input("Nhap ma sinh vien can xoa: ")
            manager.remove_student(ma_sv)

        elif chon == "3":
            ma_sv = input("Nhap ma sinh vien can sua: ")
            new_name = input("Nhap ho ten moi: ")
            manager.update_student(ma_sv, new_name)

        elif chon == "4":
            manager.display_all()

        elif chon == "5":
            print("Thoat chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()
