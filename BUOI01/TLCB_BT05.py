n = (int)(input("Nhap n: "))
if n > 0:
    if n % 2 == 0:
        print(f"{n} la so duong chan")
    else:
        print(f"{n} la so duong le")
elif n < 0 :
    if n % 2 ==0:
        print(f"{n} la so am chan")
    else:
        print(f"{n} la so am le")
elif n == 0:
    print("La so khong")