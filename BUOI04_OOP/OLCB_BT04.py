class NhanVien:
    def __init__(self, maNV="", hoTen="", luongCB=0, soNC=0):
        self.maNV = maNV
        self.hoTen = hoTen
        self.luongCB = luongCB
        self.soNC = soNC
        
    def TinhLuong(self):
        return self.luongCB * (self.soNC / 26)
    
    def HienThi(self):
        print("\nHIEN THI THONG TIN NHAN VIEN")
        print(f"Ma nhan vien: {self.maNV}")
        print(f"Ten nhan vien: {self.hoTen}")
        print(f"Luong co ba: {self.luongCB}")
        print(f"So ngay cong: {self.soNC}")
        print(f"Tien luong: {self.TinhLuong():,.2f}")
        
def main():
    nv = NhanVien("NV001", "Ho Cong Huy", 10000000, 30)
    nv.HienThi()

if __name__ == "__main__":
    main()