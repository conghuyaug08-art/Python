from abc import ABC, abstractmethod
import random

class PersonABC(ABC):
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age
        
    @abstractmethod
    def display_info(self):
        pass
    
    @abstractmethod
    def display_header(self):
        pass
    
class Person(PersonABC):
    def __init__(self, name="", age=0):
        super().__init__(name, age)
        
    def display_header(self):
        print("-" * 50)
        print(f"{'Ho ten':<25}{'Tuoi':<10}")
        
    def display_info(self):
        print(f"{self.name:<25}{self.age:<10}")
        
class Student(Person):
    def __init__(self, name="", age=0, student_id="", score=0):
        super().__init__(name, age)
        self.student_id = student_id
        self.score = score
        
    def display_header(self):
        print("-" * 70)
        print(f"{'Ma SV':<12}{'Ho ten':<25}{'Tuoi':<8}{'Diem':<10}")
        
    def display_info(self):
        print(f"{self.student_id:<12}{self.name:<25}{self.age:<8}{self.score:.2f}")
        
class Employee(Person):
    def __init__(self, name="", age=0, employee_id="", salary=0):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.salary = salary

    def display_header(self):
        print("-" * 80)
        print(f"{'Ma NV':<12}{'Ho ten':<25}{'Tuoi':<8}{'Luong':<15}")

    def display_info(self):
        print(f"{self.employee_id:<12}{self.name:<25}{self.age:<8}{self.salary:,.2f}")
    
class PersonInfo:
    def __init__(self, person):
        self.person = person
        
    def display_header(self):
        self.person.display_header()
        
    def display_info(self):
        self.person.display_info()
        
def generate_data():
    danh_sach = []
    ten = [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Van Cuong",
        "Pham Thi Dung",
        "Hoang Van Em"
    ]
    
    for i in range(5):
        if random.choice([True, False]):
            student = Student(
                ten[i],
                random.randint(18, 22),
                f"SV{i + 1:03}",
                random.uniform(5,10)
            )
            danh_sach.append(PersonInfo(student))
        else:
            employee = Employee(
                ten[i],
                random.randint(25, 40),
                f"NV{i + 1:03}",
                random.randint(7000000, 200000000)
            )
            danh_sach.append(PersonInfo(employee))
    
    return danh_sach
            
def hien_thi_student(danh_sach):
    co_student = False
    
    for person_info in danh_sach:
        if isinstance(person_info.person, Student):
            if not co_student:
                person_info.display_header()
                co_student = True             
            person_info.display_info()
    
    if not co_student:
        print("Khong co Student!")
        
def hien_thi_employee(danh_sach):
    co_employee = False
    
    for employee_info in danh_sach:
        if isinstance(employee_info.person, Employee):
            if not co_employee:
                employee_info.display_header()
                co_employee = True
            employee_info.display_info()
            
    if not co_employee:
        print("Khong co Employee!")
        
def hien_thi_tat_ca(danh_sach):
    print("\n==== DANH SACH PERSON ====")
    for person_info in danh_sach:
        person_info.display_info()
        
def them_student(danh_sach):
    print("\n==== THEM STUDENT ====")
    
    ma = input("Nhap ma sinh vien: ")
    ten = input("Nhap ten sinh vien: ")
    tuoi = int(input("Nhap tuoi: "))
    diem = float(input("Nhap diem: "))
    
    student = Student(ten, tuoi, ma, diem)
    danh_sach.append(PersonInfo(student))
    
    print("Them Student thnh cong!")
    
def them_employee(danh_sach):
    print("\n====THEM EMPLOYEE====")
    
    ma = input("Nhap ma nhan vien: ")
    ten = input("Nhap ten nhan vien vien: ")
    tuoi = int(input("Nhap tuoi: "))
    luong = float(input("Nhap luong: "))

    employee = Employee(ten, tuoi, ma, luong)
    danh_sach.append(PersonInfo(employee))

    print("Them Employee thanh cong!")

def xoa_person(danh_sach):
    ma = input("Nhap ma Student/Employee can xoa: ")

    for person_info in danh_sach:
        person = person_info.person
        
        if isinstance(person, Student) and person.student_id == ma:
            danh_sach.remove(person_info)
            print("Xoa Student thanh cong!")
            return
        
        if isinstance(person ,Employee) and person.employee_id == ma:
            danh_sach.remove(person_info)
            print("Xoa Employee thanh cong!")
            return 
    print("Khong tim thay doi tuong!")
    
def main():
    danh_sach = generate_data()

    while True:
        print("\n========== MENU ==========")
        print("1. Hien thi tat ca")
        print("2. Hien thi Student")
        print("3. Hien thi Employee")
        print("4. Them Student")
        print("5. Them Employee")
        print("6. Xoa Student/Employee")
        print("0. Thoat")
        print("==========================")

        chon = input("Nhap lua chon: ")

        if chon == "1":
            hien_thi_tat_ca(danh_sach)

        elif chon == "2":
            hien_thi_student(danh_sach)

        elif chon == "3":
            hien_thi_employee(danh_sach)

        elif chon == "4":
            them_student(danh_sach)

        elif chon == "5":
            them_employee(danh_sach)

        elif chon == "6":
            xoa_person(danh_sach)

        elif chon == "0":
            print("Ket thuc chuong trinh!")
            break

        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()