class KhachHang:
    def __init__(self, maKH="", hoTen="", loaiKH="", tongTien=0):
        self.__maKH = maKH
        self.__hoTen = hoTen
        self.__loaiKH = loaiKH
        self.__tongTien =tongTien
     
    @property
    def hoTen(self):
        return self.__hoTen
    
    @hoTen.setter
    def hoTen(self, value):
        if value.strip():
            self.__hoTen = value
        else:
            print("Ten khch hng khong duoc rong!")
    
    @property
    def tongTien(self):
        return self.__tongTien
    
    @tongTien.setter
    def tongTien(self, value):
        if(value >= 0):
            self.__tongTien = value
        else:
            print("Tong tien pahi lon hon hoac bang 0!")
            
    def TLGiamGia(self):
        if self.__loaiKH ==  "Thuong":
            return 0.0
        elif self.__loaiKH == "Bac":
            return 0.05
        elif self.__loaiKH == "Vang":
            return 0.1
        elif self.__loaiKH == "Vip":
            return 0.15
        
    def GiamGia(self):
        return self.__tongTien * self.TLGiamGia()
    
    def ThanhTien(self):
         return self.__tongTien - self.GiamGia()
     
    def Nhap(self):
        self.__maKH = input("Nhap ma khach hang: ")
        self.__hoTen = input("Nhap ten khach hang: ")
        self.__loaiKH = input("Nhap loai khaach hang: ")
        self.__tongTien = float(input("Nhap tong tien: "))        
    def Xuat(self):
        print("="*30)
        print("HIEN THI THONG TIN KHACH HANG")
        print("="*30)
        print(f"Ma khach hang: {self.__maKH}")
        print(f"Ten khach hang: {self.__hoTen}")
        print(f"Loai khach hang: {self.__loaiKH}")
        print(f"Tong tien: {self.__tongTien}")
        print(f"Ti le giam: {self.TLGiamGia()}")
        print(f"Giam gia: {self.GiamGia()}")
        print(f"Thanh tien: {self.ThanhTien()}")
        
def main():
    kh = KhachHang()
    kh.Nhap()
    kh.Xuat()

if __name__ == "__main__":
    main()
    
    
    
    
        




        
        
        
        
    
        
        
        
        
        