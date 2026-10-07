class IntergerList:
    def __init__(self):
        self.numbers = []
        
    def add_number(self, number):
        self.numbers.append(number)
        
    def remove_number(self, number):
        if number in self.numbers:
            self.numbers.remove(number)
        else:
            print("So can xoa khong ton tai!")
            
    def search_number(self, number):
        return number in self.numbers
    
    def sum_numbers(self):
        if len(self.numbers) == 0:
            return 0
        else:
            return  sum(self.numbers)
        
    def maximun(self):
        if len(self.numbers) == 0:
            print("Danh sach rong!")
            return None
        return max(self.numbers)
    
    def minimun(self):
        if len(self.numbers) == 0:
            print("Danh sach rong!")
            return None
        return min(self.numbers)
    
    def display(self):
        if len(self.numbers) == 0:
            print("Danh sach rong!")
        else:
            print("Danh sach:", self.numbers)
            
def main():
    ds = IntergerList()
    
    ds.add_number(10)
    ds.add_number(5)
    ds.add_number(20)
    ds.add_number(8)
    ds.add_number(15)
    
    print("\nDANH SACH BAN DAU")
    ds.display()
    
    print("\nTong:", ds.sum_numbers())
    print("Lon nhat:", ds.maximun())
    print("Nho nhat:", ds.minimun())
    
    print("\nTIM KIEM:")
    if ds.search_number(20):
        print("Tim thay 20")
    else:
        print("Khong tim thay 20")
    
    print("\nXOA 8:")
    ds.remove_number(8)
    ds.display()
    
    print("\nXOA 100:")
    ds.remove_number(100)
    
    print("\nSAU KHI XOA:")
    ds.display()
    
if __name__ == "__main__":
    main()
    
    