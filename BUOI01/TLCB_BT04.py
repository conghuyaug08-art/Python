string = input("Nhap chuoi: ")

doDai = len(string)
print("Do dai chuoi cua ban: ", doDai)

inHoa = string.upper()
print(inHoa)

inThuong = string.lower()
print(inThuong)

print("Xoa khoang trang dau cuoi: ", string.strip())

dem = 0
for x in string:
    if x >= "0" and x <=  "9":
        dem += 1
print("So luong ki tu so: ", dem)
    