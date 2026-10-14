from datetime import datetime
class Vehicle:
    def __init__(self, license_plate, vehicle_type):
        self.__license_plate = license_plate
        self.__vehicle_type = vehicle_type
        self.__entry_time = datetime.now()
        self.__exit_time = None
        self.__status = "Dang gui"

    @property
    def license_plate(self):
        return self.__license_plate

    @license_plate.setter
    def license_plate(self, value):
        self.__license_plate = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    @property
    def exit_time(self):
        return self.__exit_time

    @exit_time.setter
    def exit_time(self, value):
        self.__exit_time = value
   
    @property
    def vehicle_type(self):
        return self.__vehicle_type

    @vehicle_type.setter
    def vehicle_type(self, value):
        self.__vehicle_type = value

    def calculate_fee(self):
        if self.__vehicle_type == "Xe dap":
            return 3000

        elif self.__vehicle_type == "Xe may":
            return 5000

        elif self.__vehicle_type == "O to":
            return 20000

        else:
            print("Loai xe khong hop le!")
            return 0

    def display(self):
        print("\n===== THONG TIN XE =====")
        print(f"Bien so xe: {self.__license_plate}")
        print(f"Loai xe: {self.__vehicle_type}")
        print(f"Thoi gian vao bai: {self.__entry_time}")
        
        if self.__exit_time is not None:
            print(f"Thoi gian ra bai: {self.__exit_time}")
        else:
            print("Thoi gian ra bai: Chua ra bai!")
        print(f"Trang thai: {self.__status}")

        if self.__exit_time is not None:
            print(f"Tien gui xe: {self.calculate_fee()} dong")

class ParkingManager:
    def __init__(self):
        self.__vehicles = []

    def check_in(self, vehicle):
        for xe in self.__vehicles:
            if xe.license_plate == vehicle.license_plate and xe.status == "Dang gui":
                print("Xe dang duoc gui trong bai!")
                return
        self.__vehicles.append(vehicle)
        print("Check in thanh cong!")

    def find_vehicle(self, license_plate):
        for xe in self.__vehicles:
            if xe.license_plate == license_plate:
                print("Tim thay xe!")
                return xe
        print("Khong tim thay xe!")
        return None

    def check_out(self, license_plate):
        xe = self.find_vehicle(license_plate)

        if xe is None:
            return

        if xe.status != "Dang gui":
            print("xe khong co trong bai!")
            return

        xe.exit_time = datetime.now()
        xe.status = "Da lay"

        print("Check out thanh cong!")
        print(f"Tien gui xe: {xe.calculate_fee()}")

    def display_vehicles(self):
        found = False
    
        for xe in self.__vehicles:
            if xe.status == "Dang gui":
                xe.display()
                found = True

        if not found:
            print("Hien tai khong co xe nao trong bai!")

    def find_by_type(self, vehicle_type):
        found = False

        for xe in self.__vehicles:
            if xe.vehicle_type == vehicle_type:
                xe.display()
                found = True

        if not found:
            print("Khong tim thay xe!")

    def count_vehicles(self):
        xe_dap = 0
        xe_may = 0
        o_to = 0

        for xe in self.__vehicles:
            if xe.status != "Dang gui":
                continue

            if xe.vehicle_type == "Xe dap":
                xe_dap +=1
            elif xe.vehicle_type == "Xe may":
                xe_may +=1
            elif xe.vehicle_type == "O to":
                o_to +=1

        print(f"Xe dap: {xe_dap}")
        print(f"Xe may: {xe_may}")
        print(f"O to: {o_to}")

    def total_revenue(self):
        total = 0

        for xe in self.__vehicles:
            if xe.status == "Da lay":
                total += xe.calculate_fee()

        print(f"Tong doanh thu: {total} dong")
    
def main():
    bai_xe = ParkingManager()

    xe1 = Vehicle("59A1-12345", "Xe dap")
    xe2 = Vehicle("59B2-67890", "Xe may")
    xe3 = Vehicle("51C3-11111", "O to")

    print("=== 1. GUI XE ===")
    bai_xe.check_in(xe1)
    bai_xe.check_in(xe2)
    bai_xe.check_in(xe3)

    print("\n=== 2. KIEM TRA XE TRUNG BIEN SO ===")
    xe4 = Vehicle("59A1-12345", "Xe dap")
    bai_xe.check_in(xe4)

    print("\n=== 3. TIM XE ===")
    bai_xe.find_vehicle("59B2-67890")

    print("\n=== 4. DANH SACH XE TRONG BAI ===")
    bai_xe.display_vehicles()

    print("\n=== 5. TIM XE THEO LOAI ===")
    bai_xe.find_by_type("Xe may")

    print("\n=== 6. DEM SO LUONG XE ===")
    bai_xe.count_vehicles()

    print("\n=== 7. LAY XE RA ===")
    bai_xe.check_out("59A1-12345")
    bai_xe.check_out("59B2-67890")

    print("\n=== 8. DANH SACH XE CON TRONG BAI ===")
    bai_xe.display_vehicles()

    print("\n=== 9. DOANH THU ===")
    bai_xe.total_revenue()


if __name__ == "__main__":
    main() 