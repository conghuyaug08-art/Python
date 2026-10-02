from datetime import date
hoten = input("Nhap ho va ten: ")
namsinh = int(input("Nhap nam sinh: "))
namhientai = date.today().year
if namsinh > namhientai:
    namsinh = int(input("nhap lai nam sinh: "))
chuahoa = " ".join(hoten.split()).title()
tuoi = namhientai - namsinh
print("Ho Ten: " + chuahoa + "\nTuoi: " + str(tuoi))



