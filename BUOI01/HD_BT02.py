def taxi():
    passengers = (int)(input("Nhap vao so nguoi: "))
    distance = (float)(input("Nhap vao so km: "));
    total = 2*passengers + 1.5*distance
    print("Total: ", total)
taxi()
