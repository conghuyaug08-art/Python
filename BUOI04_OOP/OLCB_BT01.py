import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Bán kính không thể là số âm")
        self._radius = value
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def area(self):
        return math.pi * self.radius**2
    
    def display(self):
        print(f"Bán kính: {self.radius}")
        print(f"Chu vi: {self.perimeter()}")
        print(f"Diện tích: {self.area()}")

def main():
    radius = float(input("Nhập bán kính: "))
    c = Circle(radius)
    c.display()

if __name__ == "__main__":
    main()