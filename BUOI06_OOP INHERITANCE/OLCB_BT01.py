import math
class Hinh:
    def __init___(self):
        pass
    
    def tinh_chu_vi(self):
        return 0
    
    def tinh_dien_tich(self):
        return 0
    
    def hien_thi(self):
        print("Hinh hoc")
        
class HinhVuong(Hinh):
    def __init__(self, chieu_dai_canh = 0):
        super().__init__()
        self.chieu_dai_canh = chieu_dai_canh
        
    def nhap_thong_tin(self):
        while True:
            self.chieu_dai_canh = float(input("Nhap chieu dai canh: "))
            if self.chieu_dai_canh > 0:
                break
            print("Canh phai lon hon 0")
            
    def tinh_chu_vi(self):
        return self.chieu_dai_canh * 4
    
    def tinh_dien_tich(self):
        return self.chieu_dai_canh ** 2
    
    def hien_thi(self):
        print("--" * 30)
        print("HINH VUONG")
        print(f"Canh: {self.chieu_dai_canh:.2f}")
        print(f"Chu vi: {self.tinh_chu_vi():.2f}")
        print(f"Tinh dien tich: {self.tinh_dien_tich():.2f}")
        
class HinhChuNHat(Hinh):
    def __init__(self, chieu_dai = 0, chieu_rong = 0):
        super().__init__()
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong
        
    def nhap_thong_tin(self):
        while True:
            self.chieu_dai = float(input("Nhap chieu dai canh: "))
            if self.chieu_dai > 0:
                break
            print("Canh phai lon hon 0")
            
        while True:
            self.chieu_rong = float(input("Nhap chieu rong canh: "))
            if self.chieu_rong > 0:
                break
            print("Canh phai lon hon 0")
            
    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2
    
    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong
    
    def hien_thi(self):
        print("-" * 30)
        print("HINH CHU NHAT")
        print(f"Chieu dai: {self.chieu_dai}")
        print(f"Chieu rong: {self.chieu_rong}")
        print(f"Chu vi: {self.tinh_chu_vi():.2f}")
        print(f"Dien tich: {self.tinh_dien_tich():.2f}")
        
class HinhTron(Hinh):
    def __init__(self, ban_kinh = 0):
        super().__init__()
        self.ban_kinh = ban_kinh
        
    def nhap_thong_tin(self):
        while True:
            self.ban_kinh = float(input("Nhap ban kinh: "))
            if self.ban_kinh > 0:
                break
            print("Ban kinh phai lon hon 0!")
    
    def tinh_chu_vi(self):
        return 2 * math.pi * self.ban_kinh
    
    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2
    
    def hien_thi(self):
        print("-" * 30)
        print("HINH TRON")
        print(f"Ban kinh: {self.ban_kinh}")
        print(f"Chu vi: {self.tinh_chu_vi():.2f}")
        print(f"Dien tich: {self.tinh_dien_tich():.2f}")

class HinhTamGiac(Hinh):
    def __init__(self, a=0, b=0, c=0):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        
    def kiem_tra_hop_le(self):
        return (
            self.a > 0 and
            self.b > 0 and
            self.c > 0 and
            self.a + self.b > self.c and
            self.a + self.c > self.b and
            self.b + self.c > self.a
        )
        
    def nhap_thong_tin(self):
        while True:
            self.a = float(input("Nhap canh a: "))
            self.b = float(input("Nhap canh b: "))
            self.c = float(input("Nhap canh c: "))
            
            if self.kiem_tra_hop_le():
                break
            
            print("Ba canh khong hop le!")
            
    def tinh_chu_vi(self):
        return self.a + self.b + self.c 
    
    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p*(p-self.a)*(p-self.b)*(self.c))
    
    def hien_thi(self):
       print("-" * 30)
       print("HINH TAM GIAC")
       print(f"Canh a: {self.a}")
       print(f"Canh b: {self.b}")
       print(f"Canh c: {self.c}")
       print(f"Chu vi: {self.tinh_chu_vi():.2f}")
       print(f"Dien tich: {self.tinh_dien_tich():.2f}")
       
def menu():
    print("\n========== MENU ==========")
    print("1. Them hinh vuong")
    print("2. Them hinh chu nhat")
    print("3. Them hinh tron")
    print("4. Them hinh tam giac")
    print("5. Hien thi danh sach")
    print("6. Tim hinh co dien tich lon nhat")
    print("0. Thoat")
    print("==========================")
    
def main():
    danh_sach = []
    while True:
        menu()
        chon = int(input("Nhap luaa chon: "))
        
        if (chon == 1):
            hinh = HinhVuong()
            hinh.nhap_thong_tin()
            danh_sach.append(hinh)
            print("Them thanh cong!")
            
        elif (chon == 2):
            hinh = HinhChuNHat()
            hinh.nhap_thong_tin()
            danh_sach.append(hinh)
            print("Them thanh cong!")
            
        elif (chon == 3):
            hinh = HinhTron()
            hinh.nhap_thong_tin()
            danh_sach.append(hinh)
            print("Them thanh cong!")
            
        elif (chon == 4):
            hinh = HinhTamGiac()
            hinh.nhap_thong_tin()
            danh_sach.append(hinh)
            print("Them thanh cong!")
            
        elif (chon == 5):
            if len(danh_sach) == 0:
                print("Danh sach rong!")
            else:
                for hinh in danh_sach:
                    hinh.hien_thi()
        
        elif (chon == 6):
            if len(danh_sach) == 0:
                print("Danh sach rong")
            
            else:
                hinh_max = danh_sach[0]
                
                for hinh in danh_sach:
                    if hinh.tinh_dien_tich() > hinh_max.tinh_dien_tich():
                        hinh_max = hinh
                        
            print("\nHINH CO DIEN TICH LON NHAT")
            hinh_max.hien_thi()
            
        elif (chon == 0):
            print("Ket thuc chuong trinh!")
            break
        
        else:
            print("Lua chon khong hop le!")
            
if __name__ == "__main__":
    main()
    
            
            
    
        
        
        
        