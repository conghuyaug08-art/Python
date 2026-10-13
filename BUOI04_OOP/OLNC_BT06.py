class StudentGrade:
    def __init__(self, student_id="", name=""):
        self.student_id = student_id
        self.name = name
        self.grades = {}

    def TinhDTB(self):
        return (self.grades["Toan"] * 2 + self.grades["Van"] * 2 + self.grades["Anh"]) / 5

class GradeBook:
    def __init__(self):
        self.students = []

    def AddStudent(self, student):
        self.students.append(student)
        print("Them hoc sinh thanh cong!")

    def CalculateAverage(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student.TinhDTB()
        print("Khong tim thay hoc sinh")
        return None

    def FindTopStudent(self):
        if not self.students:
            print("Danh sach rong!")
            return None
        maxDiem = self.students[0]
        for student in self.students:
            if student.TinhDTB() > maxDiem.TinhDTB():
                maxDiem = student
        return maxDiem

    def DisplayReportCard(self):
        dsSapXep = sorted(self.students, key=lambda student: student.TinhDTB(), reverse=True)
        print("\nBANG DIEM HOC SINH")
        print("=" * 50)
        for student in dsSapXep:
            print(f"Ma hoc sinh: {student.student_id}")
            print(f"Ho ten: {student.name}")
            print(f"Diem Toan:", student.grades["Toan"])
            print(f"Diem Van:", student.grades["Van"])
            print(f"Diem Anh:", student.grades["Anh"])
            print(f"Diem trung binh:", student.TinhDTB())
            print("=" * 50)

def main():
    hs1 = StudentGrade("HS001", "Uchihapvy")
    hs2 = StudentGrade("HS002", "Uzumakihi")

    hs1.grades = {"Toan": 8, "Van": 7, "Anh": 9}
    hs2.grades = {"Toan": 9, "Van": 8, "Anh": 7}

    gb = GradeBook()
    gb.AddStudent(hs1)
    gb.AddStudent(hs2)
    gb.DisplayReportCard()

    top = gb.FindTopStudent()
    if top is not None:
        print("Hoc sinh diem cao nhat:", top.name)


if __name__ == "__main__":
    main()
