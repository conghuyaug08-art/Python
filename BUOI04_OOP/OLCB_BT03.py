class Student:
    def __init__(self, student_id="", full_name="", age=1, gpa=0):
        self.student_id = student_id
        self.full_name = full_name
        self.age = age
        self.gpa = gpa
        
    @property
    def student_id(self):
        return self._student_id
    
    @student_id.setter
    def student_id(self, value):
        self._student_id = value
        
    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, value):
        self._full_name = value
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value > 0:
            self._age = value
        else:
            raise ValueError("Tuoi phai lon hon 0")    
    
    @property
    def gpa(self):
        return self._gpa
    
    @gpa.setter
    def gpa(self, value):
        if 0 <= value <= 10:
            self._gpa = value
        else:
            raise ValueError("GPA phai nam trong khoang 0 den 10")
        
    def input__info(self):
        self.student_id = input("Nhap ma hoc sinh: ")
        self.full_name = input("Nhap ten hoc sinh: ")
        self.age = int(input("Nhap tuoi hoc sinh: "))
        self.gpa = float(input("Nhap diem GPA: "))
        
    def is__sholarship(self):
        if self.gpa >= 8:
            print("Du dieu kien nhan hoc bong!")
        else:
            print("Khong du dieu kien nhan hoc bong")
            
    def display(self):
        print("\nHIEN THI THONG TIN")
        print(f"Student id: {self._student_id}")
        print(f"Full name: {self._full_name}")
        print(f"Age: {self._age}")
        print(f"GPA: {self._gpa}")
        self.is__sholarship()
        
def main():
    hs = Student()
    hs.input__info()
    hs.display()

if __name__ == "__main__":
    main()