class Employee:
    def __init__(self, maNV="", hoTen="", phongBan="", luongCB=0, soGioLam=0):
        self.maNV = maNV
        self.hoTen = hoTen
        self.phongBan = phongBan
        self.luongCB = luongCB
        self.soGioLam = soGioLam
        
    def bonus(self):
        if self.soGioLam > 160:
            return self.luongCB * 0.1
        return 0
    
    def income(self):
        return self.luongCB + self.bonus()
    
    def input_info(self):
        self.maNV = input("Nhap ma nhan vien: ")
        self.hoTen = input("Nhap ho ten: ")
        self.phongBan = input("Nhap phong ban: ")
        self.luongCB = float(input("Nhap luong co ban: "))
        self.soGioLam = float(input("Nhap so gio lam: "))
    
    def display(self):
       print("-" * 30)
       print(f"Ma nhan vien: {self.maNV}")
       print(f"Ho ten: {self.hoTen}")
       print(f"Phong ban: {self.phongBan}")
       print(f"Luong co ban: {self.luongCB:,.2f}")
       print(f"So gio lam: {self.soGioLam}")
       print(f"Tien thuong: {self.bonus():,.2f}")
       print(f"Tong thu nhap: {self.income():,.2f}")

class EmployeeManager:
    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        if self.find_employee(employee.maNV) is not None:
            print("Ma nhan vien da ton tai!")
        else:
            self.employees.append(employee)
            print("Da them nhaan vien thanh cong!")
            
    def find_employee(self, maNV):
        for employee in self.employees:
            if employee.maNV == maNV:
                return employee
        return None
    
    def update_salary(self, maNV, luongMoi):
        employee = self.find_employee(maNV)
        
        if employee is not None:
            employee.luongCB = luongMoi
            print("Cap nhat luong thanh cong!")
        else:
            print("Khong tim thay nhan vien!")
            
    def delete_employee(self, maNV):
        employee = self.find_employee(maNV)
        
        if employee is not None:
            self.employees.remove(employee)
            print("Xoa nhan vien thanh cong!")
        else:
            print("Khong tim thay nhan vien!")
            
    def sort_by_income(self):
        self.employees.sort(key=lambda employee: employee.income(), reverse=True)
     
    def deparment_statistics(self):
        statistics = {}
        
        for employee in self.employees:
            if employee.phongBan in statistics:
                statistics[employee.phongBan] += 1
            else:
                statistics[employee.phongBan] = 1
        
        print("\nTHONG KE THEO PHONG BAN")
        for phongBan, soLuong in statistics.items():
            print(f"{phongBan}: {soLuong} nhan vien")
            
def main():
    manager = EmployeeManager()

    while True:
        print("\n========== MENU ==========")
        print("1. Them nhan vien")
        print("2. Tim nhan vien")
        print("3. Cap nhat luong")
        print("4. Xoa nhan vien")
        print("5. Hien thi danh sach")
        print("6. Sap xep theo thu nhap")
        print("7. Thong ke theo phong ban")
        print("0. Thoat")
        print("==========================")

        chon = input("Nhap lua chon: ")
        
        if chon == "1":
            employee = Employee()            
            employee.input_info()
            
            manager.add_employee(employee)
        
        elif chon == "2":
            maNV = input("Nhap ma nhan vien can tim: ")
            
            employee = manager.find_employee(maNV)
            if employee is not None:
                employee.display()
            else:
                print("Khong tim thay nhan vien!")
                
        elif chon == "3":
            maNV = input("Nhap ma nhan vien: ")
            luongMoi = float(input("Nhap luong moi: "))
            
            manager.update_salary(maNV, luongMoi)
            
        elif chon == "4":
            maNV = input("Nhap ma nhan vien: ")
            
            manager.delete_employee(maNV)
            
        elif chon == "5":
            if len(manager.employees) == 0:
                print("Danh sach nhan vien rong!")
            else:
                print("\nDANH SACH NHAN VIEN")
                
                for employee in manager.employees:
                    employee.display()
                    
        elif chon == "6":
            manager.sort_by_income()
            
            print("Da sap xep theo thu nhap giam dan")
            
            for employee in manager.employees:
                print(
                    f"{employee.maNV} - "
                    f"{employee.hoTen} -"
                    f"{employee.income():,.2f}"
                )
                
        elif chon == "7":
            manager.deparment_statistics()
            
        elif chon == "0":
            print("Ket thuc chuong trinh!")
            break
        
        else:
            print("Lua chon khong hop le!")
            
if __name__ == "__main__":
    main()
            
            
            
            
            
            
                
            
            

        
        
                
            
    
        