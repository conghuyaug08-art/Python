import math
class PhanSo:
    def __init__(self, tuso=0, mauso = 1):
        self.tuso = tuso
        self.mauso = mauso
        
    def NhapPS(self):
        self.tuso = int(input("Nhap vao tu so: "))
        while True:            
            self.mauso = int(input("Nhap vao mau so: "))
            if self.mauso != 0:
                break
            print("Mau so phai khac 0!")
        
    def RutGonPS(self):
        ucln = math.gcd(self.tuso, self.mauso)
        self.tuso = self.tuso // ucln
        self.maauso = self.mauso // ucln
        if self.mauso < 0:
            self.tuso = - self.tuso
            self.mauso = -self.mauso
            
    def GiaTri(self):
        return self.tuso / self.mauso
    
    def HienThi(self):
        print(f"Phan so: {self.tuso}/{self.mauso}")
        print(f"Gia tri: {self.GiaTri()}")
        
def main():
    ps = PhanSo()
    ps.NhapPS()
    ps.HienThi()
    
    ps.RutGonPS()
    print("Phan so sau khi rut gon")
    ps.HienThi()
    
if __name__ == "__main__":
    main()
        
        