from datetime import datetime, date

class Person:
    def __init__(self, hoTen="", quocGia="", ngaySinh=None):
        self.__hoTen = hoTen
        self._quocGia = quocGia
        self.__ngaySinh = ngaySinh

    def get_ho_ten(self):
        return self.__hoTen

    def set_ho_ten(self, hoTen):
        if hoTen.strip():
            self.__hoTen = hoTen
        else:
            print("Ho ten khong duoc rong!")
            
    def get_ngay_sinh(self):
        return self.__ngaySinh
    
    def set_ngay_sinh(self, ngaySinh):
        if(ngaySinh <= date.today()):
            self.__ngaySinh = ngaySinh
        else:
            print("Ngay sinh khong duoc lon hon ngay hien tai!")
    
    def TinhTuoi(self):
        today = date.today()
        
        tuoi = today.year - self.__ngaySinh.year
        if(today.day, today.month) < (self.__ngaySinh.day, self.__ngaySinh.month):
            tuoi -= 1
            
        return tuoi
    
    def HienThi(self):
        print("-" * 30)
        print("THONG TIN PERSON")
        print("-" * 30)
        print(f"Ho ten: {self.__hoTen}")
        print(f"Quoc gia: {self._quocGia}")
        print(f"Ngay sinh: {self.__ngaySinh.strftime('%d/%m/%Y')}")
        print(f"Tuoi: {self.TinhTuoi()}")
        
def main():
    ngaysinh = datetime.strptime("07/05/2007", "%d/%m/%Y").date()
    p = Person("Nguyen Van A", "Vietnam", ngaysinh)
    p.HienThi()
    
    print("Ho ten hien tai: ", p.get_ho_ten())
    p.set_ho_ten("Tran Van C")
    print("Ho ten sau khi thay doi: ", p.get_ho_ten())
    
    print("Truy cap truc tiep _quocGia:", p._quocGia)
    print("Truy cap truc tiep __hoTen:")
    try:
        print(p.__hoTen)
    except AttributeError:
        print("=> Khong the truy cap truc tiep __hoTen")
if __name__ == "__main__":
    main()
    
        
            
    
        