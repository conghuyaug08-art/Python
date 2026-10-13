class Event:
    def __init__(self, event_id="", name="", date="", ticket_price=0, total_tickets=0):
        self.event_id = event_id
        self.name = name
        self.date = date
        self.ticket_price = ticket_price
        self.total_tickets = total_tickets
        self.sold_tickets = 0

class EventOrganizer:
    def __init__(self):
        self.list_events = []

    def sell_ticket(self, event_id, quantity):
        if quantity <= 0:
            print("So luong mua phai lon hon 0")
            return
        
        for event in self.list_events:
            if event.event_id == event_id:
                veConLai = event.total_tickets - event.sold_tickets
                if veConLai >= quantity:
                    # Cap nhat so ve da ban]
                    event.sold_tickets += quantity

                    # So ve con lai
                    veConLai = event.total_tickets - event.sold_tickets                   
                    print("Ban ve thanh cong! So ve con lai:", veConLai)
                    return 
                else:
                    print("Het ve!")
                    return 
        
        print("Khong tim thay ma su kien!")

    def calculate_event_revenue(self, event_id):
        doanh_thu = 0
        for event in self.list_events:
            if event.event_id == event_id:
                doanh_thu += event.sold_tickets * event.ticket_price
                return doanh_thu

        print("Khong tim thay ma su kien!")
        return 0

    def display_active_events(self):
        print(f"{'Ma su kien':<15}{'Ten su kien':<30}{'Ngay to chuc':<15}{'Ve da ban':<15}{'Ty le lap day':<10}")
        for event in self.list_events:
            if event.total_tickets != 0:
                ty_le_lap_day = event.sold_tickets / event.total_tickets * 100
            else:
                ty_le_lap_day = 0
            print(f"{event.event_id:<15}{event.name:<30}{event.date:<15}{str(event.sold_tickets) + '/' + str(event.total_tickets):<15}{ty_le_lap_day:<5.2f}%")

    def add_event(self, event):
        self.list_events.append(event)
        print("Them thanh cong!")

def main():
    QLSK =  EventOrganizer()
    sk1 = Event("SK001", "Trai Buon Nguoi", "16/10/2026", 65000, 2)
    sk2 = Event("SK002", "An banh Aeon", "16/10/2026", 40000, 2)
    
    QLSK.add_event(sk1)
    
    QLSK.add_event(sk2)
    
    QLSK.display_active_events()

    QLSK.sell_ticket("SK001", 1)

    print("Doanh thu:", QLSK.calculate_event_revenue(sk1.event_id))
    
    QLSK.display_active_events()

if __name__ == "__main__":
    main()


        




    