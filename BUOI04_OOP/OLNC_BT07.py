class Flight:
    def __init__(self, flight_code="", destination="", total_seats=0):
        self.flight_code = flight_code
        self.destination = destination
        self.total_seats = total_seats
        self.booked_seats = []

    def book_seat(self, passenger_name):
        if len(self.booked_seats) >= self.total_seats:
            print("Khong con du cho!")
            return False

        self.booked_seats.append(passenger_name)
        print("Dat ghe thnh cong!")
        return True

    def cancel_seat(self, passenger_name):
        if passenger_name in self.booked_seats:
            self.booked_seats.remove(passenger_name)
            print("Huy dat cho thanh cong!")
            return True
        else:
            print("Khong tim thaay khach hang!")
            return False

    def is_full(self):
        if len(self.booked_seats) >= self.total_seats:
            return True
        return False


def main():
    flight1 = Flight("VN001", "Ha Noi", 2)
    flight2 = Flight("VN002", "Da Nang", 3)
    flight3 = Flight("VN003", "Can Tho", 1)

    flight1.book_seat("Nguyen Van A")
    flight1.book_seat("Tran Van B")
    flight1.book_seat("Le Van C")

    flight2.book_seat("Pham Thi D")
    flight2.book_seat("Ho Van E")

    flight3.book_seat("Nguyen Van F")

    print("\nKiem tra trang thai chuyen bay:")
    print(flight1.flight_code, flight1.is_full())
    print(flight2.flight_code, flight2.is_full())
    print(flight3.flight_code, flight3.is_full())

    print("\nHuy dat cho:")
    flight1.cancel_seat("Nguyen Van A")

    print("\nKiem tra lai chuyen bay VN001:")
    print(flight1.flight_code, flight1.is_full())


if __name__ == "__main__":
    main()

