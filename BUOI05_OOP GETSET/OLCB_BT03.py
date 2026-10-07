class SoPhuc:
    def __init__(self, thuc=0, ao=0):
        self.__thuc = thuc
        self.__ao = ao
        
    @property
    def thuc(self):
        return self.__thuc
    
    @thuc.setter
    def thuc(self, value):
        self.__thuc = value
        
    @property
    def ao(self):
        return self.__ao
    
    @ao.setter
    def ao(self, value):
        self.__ao = value
        
    def Nhap(self):
        self.__thuc = int(input("Nhap phan thuc: "))
        self.__ao = int(input("Nhap phan ao: "))
    
    def Xuat(self):
        if (self.__ao > 0):
            print(f"{self.__thuc} + {self.__ao}i")
        else:
            print(f"{self.__thuc} - {self.__ao}i")
            
    def Cong(self, other):
        thuc =(self.__thuc + other.__thuc) 
        ao = (self.__ao + other.__ao)
        return SoPhuc(thuc, ao)

    def Tru(self, other):
        thuc = (self.__thuc - other.__thuc)
        ao =(self.__ao - other.__ao)
        return SoPhuc(thuc, ao)
    
def main():
    p1 = SoPhuc()
    p1.Nhap()
    p2 = SoPhuc()
    p2.Nhap()
    print("SO PHUC 1:")
    p1.Xuat()
    print("SO PHUC 2:")
    p2.Xuat()
    
    print("\nGETTER")
    print("Phan thuc: ", p1.thuc)
    print("Phan ao: ", p1.ao)
    
    print("\nSETTER")
    p1.thuc = 5
    p1.ao = 10
    print("So thuc 1 sau khi thay doi")
    p1.Xuat()
    
    print("\nPHEP CONG:")
    tong = p1.Cong(p2)
    tong.Xuat()
    
    print("\nPHEP Tru:")
    tru = p1.Tru(p2)
    tru.Xuat()
    
if __name__ == "__main__":
    main()
    
    
    
    
    

    
             
        