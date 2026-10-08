class HotelRoom:
    def __init__(self, room_number="", room_type="", price_per_night=0, is_available=True):
        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.is_available = is_available
        
    def display(self):
        trang_thai = "Trong" if self.is_available else "Da dat"
        print(f"Phong {self.room_number} - {self.room_type} - "
              f"{self.price_per_night:,.0f} VND/ dem - {trang_thai}")


class HotelManager:
    def __init__(self):
        self.rooms = []
        
    def add_room(self, room):
        self.rooms.append(room)
        print("Them phong thanh cong!")
        
    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_available:
                    room.is_available = False
                    print(f"Da dat phong {room_number}.")
                else:
                    print(f"Phong {room_number} da duoc dat!")
                return
                
        print(f"Khong tim thay phong {room_number}.")
        
    def check_out(self, room_number, nights):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_available:
                    total = room.price_per_night * nights
                    room.is_available = True
                    
                    print(f"Tra phong {room_number} thanh cong.")
                    print(f"So dem: {nights}")
                    print(f"Tong tien: {total:,.0f} VND")
                else:
                    print(f"Phong {room_number} dang trong!")
                return
        
        print(f"Khong tim thay phong {room_number}.")

    def find_available_rooms(self):
        print("\nDANH SACH PHONG TRONG")
        print("-" * 50)
        
        found = False
        
        for room in self.rooms:
            if room.is_available:
                room.display()
                found = True
                
        if not found:
            print("Khong co phong trong.")


def main():
    manager = HotelManager()
    
    while True:
        print("\n========== QUAN LY KHACH SAN ==========")
        print("1. Them phong")
        print("2. Dat phong")
        print("3. Tra phong")
        print("4. Hien thi phong trong")
        print("0. Thoat")
        print("=======================================")
        
        choice = input("Nhap lua chon: ")
        
        if choice == "1":
            room_number = input("Nhap so phong: ")
            room_type = input("Nhap loai phong (Standard/Deluxe/Suite): ")
            price = float(input("Nhap gia phong moi dem: "))
            
            room = HotelRoom(room_number, room_type, price)
            manager.add_room(room)
            
        elif choice == "2":
            room_number = input("Nhap so phong can dat: ")
            manager.book_room(room_number)
            
        elif choice == "3":
            room_number = input("Nhap so phong can tra: ")
            nights = int(input("Nhap so dem: "))
            manager.check_out(room_number, nights)
            
        elif choice == "4":
            manager.find_available_rooms()
            
        elif choice == "0":
            print("Da thoat chuong trinh.")
            break
            
        else:
            print("Lua chon khong hop le!")


if __name__ == "__main__":
    main()