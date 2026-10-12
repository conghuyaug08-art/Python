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
class OrderItem:
    def __init__(self, product="", quantity=0):
        self.product = product
        self.quantity = quantity

    def ThanhTien(self):
        return self.product.gia * self.quantity

class Order:
    def __init__(self, order_id="", voucher_discount=0):
        self.order_id = order_id
        if 0 <= voucher_discount <= 50:
            self.voucher_discount = voucher_discount
        else:
            raise ValueError("Voucher phai tu 0% den 50%")
        
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print("Them thanh cong!")

    def calculate_total(self):
        tongTien = 0
        
        for item in self.items:
            tongTien += item.ThanhTien()

        
        voucher = self.voucher_discount
        return tongTien - voucher / 100 * tongTien

    def display_order(self):
        print("=" * 50)
        print("HOA DON BAN LE")
        print(f"Ma don hang:  {self.order_id}")
        print("=" * 50)

        for item in self.items:
            print(f"Ten san pham: {item.product.tenSP}")
            print(f"So luong: {item.quantity}")
            print(f"Don gia: {item.product.gia:,.0f} VND")
            print(f"Thanh tien tung mat hang: {item.ThanhTien():,.0f} VND")
            print("=" * 50)
        
        tongTien = 0
        for item in self.items:
            tongTien += item.ThanhTien()

        tienGiam = tongTien * self.voucher_discount / 100

        print(f"Tong tien hang: {tongTien:,.0f} VND")
        print(f"Voucher giam gia: {self.voucher_discount}%")
        print(f"Tien duoc giam: {tienGiam:,.0f} VND")
        print(f"TONG THANH TOAN: {self.calculate_total():,.0f} VND")
        print("=" * 50)
        print("Cam on quy khach!")

def main():
    sp1 = SanPham("SP001", "So cong Klong", 100000, 20)
    sp2 = SanPham("SP002", "Giay ve A3", 50000, 50)

    mh1 = OrderItem(sp1, 40)
    mh2 = OrderItem(sp2, 10)

    dh = Order("DH001", 10)

    dh.add_item(mh1)
    dh.add_item(mh2)

    dh.display_order()

    
if __name__ == "__main__":
    main()