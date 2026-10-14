from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __init__(self, ten_hinh):
        self.ten_hinh = ten_hinh

    @abstractmethod
    def tinh_dien_tich(self):
        pass

    @abstractmethod
    def tinh_chu_vi(self):
        pass

class Circle(Shape):
    def __init__(self, ban_kinh):
        super().__init__("Hinh tron")
        self.ban_kinh = ban_kinh

    def tinh_dien_tich(self):
        return math.pi * self.ban_kinh ** 2

    def tinh_chu_vi(self):
        return 2* math.pi * self.ban_kinh

class Rectangle(Shape):
    def __init__(self, chieu_dai, chieu_rong):
        super().__init__("Hinh chu nhat")
        self.chieu_dai = chieu_dai
        self.chieu_rong = chieu_rong

    def tinh_dien_tich(self):
        return self.chieu_dai * self.chieu_rong

    def tinh_chu_vi(self):
        return (self.chieu_dai + self.chieu_rong) * 2

class Triangle(Shape):
    def __init__(self, a, b, c):
        super().__init__("Hinh tam giac")

        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Ba canh phai lon hon 0")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Ba canh khong tao thanh tam giac")

        self.a = a
        self.b = b
        self.c = c

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() / 2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

    def tinh_chu_vi(self):
        return self.a + self.b + self.c

def main():
    ds_hinh = [
        Circle(5),
        Rectangle(4, 6),
        Triangle(3, 4, 5)
    ]

    tong_dien_tich = 0

    for hinh in ds_hinh:
        print("Ten hinh:", hinh.ten_hinh)
        print("Chu vi:", round(hinh.tinh_chu_vi(), 2))
        print("Dien tich:", round(hinh.tinh_dien_tich(), 2))
        print("--------------------")

        tong_dien_tich += hinh.tinh_dien_tich()

    print("Tong dien tich:", round(tong_dien_tich, 2))


if __name__ == "__main__":
    main()  