class NhanVien:
    def __init__(self, ma_nv="", ho_ten="", luong_co_ban=0):
        self.ma_nv = ma_nv
        self.ho_ten = ho_ten
        self.luong_co_ban = luong_co_ban

    def nhap_thong_tin(self):
        self.ma_nv = input("Nhap ma nhan vien: ")
        self.ho_ten = input("Nhap ho ten: ")

        while True:
            try:
                luong = float(input("Nhap luong co ban: "))
                if luong > 0:
                    self.luong_co_ban = luong
                    break
                print("Luong co ban phai lon hon 0!")
            except ValueError:
                print("Vui long nhap so hop le!")

    def tinh_luong(self):
        return self.luong_co_ban

    def tinh_thue(self):
        luong = self.tinh_luong()
        if luong >= 15000000:
            return luong * 0.05
        return 0

    def tinh_thuc_lanh(self):
        return  self.tinh_luong() - self.tinh_thue()

    def hien_thi(self):
        print(f"Ma nhan vien: {self.ma_nv}")
        print(f"Ho ten: {self.ho_ten}")
        print(f"Luong co ban: {self.luong_co_ban:,.0f} VND")
        print(f"Tien luong: {self.tinh_luong():,.0f} VND")
        print(f"Tien thue: {self.tinh_thue():,.0f} VND")
        print(f"Thuc lanh: {self.tinh_thuc_lanh():,.0f} VND")

class NhanVienVanPhong(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, so_ngay_lam):
        super().__init__(ma_nv, ho_ten, luong_co_ban)
        while True:
            try:
                ngay = int(input("Nhap so ngay lam: "))
                if ngay >= 0:
                    self.so_ngay_lam = ngay
                    break
                print("So ngay lam phai la so nguyen khong am")
            except ValueError:
                print("Vui long nhap so hop le!")

    def tinh_luong(self):
        return self.luong_co_ban + self.so_ngay_lam * 200000

class NhanVienKinhDoanh(NhanVien):
    def __init__(self, ma_nv, ho_ten, luong_co_ban, doanh_so):
        super().__init__(ma_nv, ho_ten, luong_co_ban)

        while True:
            try:
                ds = float(input("Nhap doanh so: "))
                if ds >= 0:
                    self.doanh_so = ds
                    break
                print("Doanh so phai la khong am!")
            except ValueError:
                print("Vui long nhap so hop le!")

    def tinh_hoa_hong(self):
        return self.doanh_so * 0.05

    def tinh_luong(self):
        return self.luong_co_ban + self.tinh_hoa_hong()


def main():
    danh_sach_nv = []

    print("===== NHAP NHAN VIEN VAN PHONG =====")
    nv1 = NhanVienVanPhong("VP01", "Nguyen An", 5000000, 0)
    nv2 = NhanVienVanPhong("VP02", "Tran Binh", 6000000, 0)

    print("\n===== NHAP NHAN VIEN KINH DOANH =====")
    nv3 = NhanVienKinhDoanh("KD01", "Le Cuong", 8000000, 0)
    nv4 = NhanVienKinhDoanh("KD02", "Pham Dung", 7000000, 0)

    danh_sach_nv.extend([nv1, nv2, nv3, nv4])

    print("\n========== DANH SACH NHAN VIEN ==========")
    for nv in danh_sach_nv:
        print("\n------------------------------")
        nv.hien_thi()

    tong_luong = 0
    for nv in danh_sach_nv:
        tong_luong += nv.tinh_luong()

    print("\n========== TONG QUY LUONG ==========")
    print(f"Tong quỹ lương: {tong_luong:,.0f} VND")

    nv_cao_nhat = max(danh_sach_nv, key=lambda nv: nv.tinh_luong())

    print("\n========== NHAN VIEN LUONG CAO NHAT ==========")
    nv_cao_nhat.hien_thi()


if __name__ == "__main__":
    main()


