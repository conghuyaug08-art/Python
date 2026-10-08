import math

class Point2D:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
        
    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
    
    def display(self):
        print(f"{(self.x, self.y)}")
        
def main():
    d1 = Point2D(2, 5)
    d2 = Point2D(3,6)
    print("Diem 1:")
    d1.display()
    print("Diem 2:")
    d2.display()
    kc = d1.distance_to(d2)
    print("Khoang cach: ", kc)
if __name__ == "__main__":
    main()
    
    