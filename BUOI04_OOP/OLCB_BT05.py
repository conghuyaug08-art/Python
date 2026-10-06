class SanPham:
    def __init__(self, maSP="", tenSP="", gia=0, soLuong=0):
        self.maSP = maSP
        self.tenSP = tenSP
        self.gia = gia
        self.soLuong = soLuong
        
    def ThanhTien(self):
        return self.gia * self.soLuong

    def GiamGia(self):
        if self.soLuong > 10:
            return 0.1*self.ThanhTien()
        else:
            return 0  
        
    def ThucTe(self):
        return self.ThanhTien() - self.GiamGia()
    
    def HienThi(self):
        print("HIEN THI THONG TIN SAN PHAM")
        print(f"Ma san pham: {self.maSP}")
        print(f"Ten san pham: {self.tenSP}")
        print(f"Gia: {self.gia}")
        print(f"So luong: {self.soLuong}")
        print(f"Thanh tien: {self.ThanhTien():,.2f}")
        print(f"Giam gia: {self.GiamGia():,.2f}")
        print(f"Tien thuc phai tra: {self.ThucTe():,.2f}")
        
def main():
    sp = SanPham("SP001", "COCA COLA", 100000, 20)
    sp.HienThi()
    
if __name__ == "__main__":
    main()
        
        
    