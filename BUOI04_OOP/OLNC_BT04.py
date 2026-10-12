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

class BankAccount(TaiKhoanNgaHang):
    def __init__(self, soTK="", chuTK="", soDu=0):
        super().__init__(soTK, chuTK, soDu)
        self.transaction_history = []

    def ThemGiaoDich(self, loaiGD, soTien, soDuTruoc):
        giaoDich = {
            "thoi_gian": datetime.now().strftime("%d/%m/%y %H:%M:%S"),
            "noiDung" : noiDung,
            "soTien" : soTien,
            "soDuTruoc" : soDuTruoc,
            "soDuSau" : self.soDu 
        }
        self.transaction_history.append(giaoDich)

    def RutTien(self, tienRut):
        soDuTruoc = self.soDu
        super().RutTien(tienRut)
        self.ThemGiaoDich("Rut tien", -tienRut, soDuTruoc)

    def HienThiLichSu(self):
        print(f"\nLICH SU GIAO DICH - {self.chuTK}")
        print(f"So tai khoan: {self.soTK}")

        if not self.transaction_history:
            print("Chua co giao dich. ")
            return
        for gd in self.transaction_history:
                print("-" * 50)
                print(f"Thoi gian: {gd['thoiGian']}")
                print(f"Noi dung: {gd['noiDung']}")
                print(f"So tien bien dong: {gd['soTien']:+,.0f} VND")
                print(f"So du truoc: {gd['soDuTruoc']:,.0f} VND")
                print(f"So du sau: {gd['soDuSau']:,.0f} VND")

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