class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, value):
        if value < 0:
            raise ValueError("Chieu dai phai lon hon 0")
        self._length = value
        
    @property
    def width(self):
      return self._width
  
    @width.setter
    def width(self, value):
      if value < 0:
          raise ValueError("Chieu rong phai lon hon 0")
      self._width = value    
      
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def area(self):
        return self.length * self.width
    
    def isSquare(self):
        return self.length == self.width
    
    def display(self):
        print(f"Chieu dai: {self.length}")
        print(f"Chieu rong: {self.width}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Dien tich: {self.area()}")
        print(f"Hinh vuong: {'Co' if self.isSquare() else 'Khong'}")
        
def main():
    hcn1 = Rectangle(2, 5)
    hcn2 = Rectangle(4, 4)
    
    print("Hinh chu nhat 1")
    hcn1.display()
    print("-"*20)
    print("Hinh chu nhat 2")
    hcn2.display()
    
if __name__ == "__main__":
    main()
        
    
        
    