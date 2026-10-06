class TaiKhoanNganHang:
    def __init__(self, soTK="", chuTK="", soDu=0):
        self.soTK = soTK
        self.chuTK = chuTK
        self.soDu = soDu
        
    def GuiTien(self, tienGui):
        if tienGui > 0:
            self.soDu += tienGui
        else:
            raise ValueError("So tien gui vao phai lon hon 0!")
    
    def RutTien(self, tienRut):
        if tienRut > 0 and tienRut <= self.soDu:
            self.soDu -= tienRut
        else:
            raise ValueError("So tien rut phai lon hon 0 va khong duoc lon hon so du")
        
    def HienThiSoDu(self):
        return self.soDu
    
    def HienThiTK(self):
        print("HIEN THI TAI KHOAN")
        print(f"So tai khoan: {self.soTK}")
        print(f"Ten chu tai khoan: {self.chuTK}")
        print(f"So du: {self.HienThiSoDu()}")
        
def main():
    tk = TaiKhoanNganHang("08887383", "Nguyen Van A", 100000)
    
    tk.HienThiTK()
    
    tk.GuiTien(50000)
    print("\nSau khi gui 50000:")
    tk.HienThiTK()
    
    tk.RutTien(30000)
    print("\nSau khi rut 30000:")
    tk.HienThiTK()
    
if __name__ == "__main__":
    main()