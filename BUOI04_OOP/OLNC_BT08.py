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
        print(f"Student ID: {self._student_id}")
        print(f"Full name: {self._full_name}")
        print(f"Age: {self._age}")
        print(f"GPA: {self._gpa}")
        self.is__sholarship()

class Course:
    def __init__(self, course_code="", course_name="", max_students=0):
        self.course_code = course_code
        self.course_name = course_name
        self.max_students = max_students
        self.registered_students = []

    def display_student(self):
        print(f"\nTen hoc phan: {self.course_name}")
        print(f"Ma hoc phan: {self.course_code}")
        print(f"So luong: {len(self.registered_students)}/{self.max_students}")

        if len(self.registered_students) == 0:
            print("Chua co sinh vien dang ky!")
        else:
            for student in self.registered_students:
                student.display()

    def register_gpa(self, student):
        if student.gpa < 5.0:
            print("Sinh vien khong du dieu kien dang ky!")
            return False
        return True

    def is_full(self):
        if self.max_students <= len(self.registered_students):
            print("Hoc phan da day!")
            return True
        return False
class CourseRegistration:
    def register_course(self, student, course):
        if course.is_full() == True:
            print("Hoc phan da day!")
            return False
        
        elif not course.register_gpa(student):
            print("Sinh vien khong du dieu kien dang ki!")
            return False
        else:
            course.registered_students.append(student)
            print("Them thanh cong!")
            return True

def main():
    student = Student("SV01", "Nguyen Van A", 20, 5.0)
    course = Course("IT01", "Python", 2)
    registration = CourseRegistration()

    registration.register_course(student, course)
    course.display_student()

if __name__ == "__main__":
    main()




        
    

        


    