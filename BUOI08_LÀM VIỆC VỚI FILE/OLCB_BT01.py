import os
def tao_file_mau(ten_file):
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write("10 20 30\n")
        f.write("5 15\n")
        f.write("7 8 9\n")


def doc_file(ten_file):
    with open(ten_file, "r", encoding="utf-8") as f:
        return f.read()


def tinh_tong(noi_dung):
    tong = 0

    for dong in noi_dung.splitlines():
        for so in dong.split():
            tong += float(so)

    return tong


def ghi_file(ten_file, noi_dung, tong):
    with open(ten_file, "w", encoding="utf-8") as f:
        f.write(noi_dung)
        f.write("\nTong cac so: " + str(tong))


def main():
    thu_muc = os.path.dirname(os.path.abspath(__file__))

    ten_file = os.path.join(thu_muc, "OLop01_danh_sach_so.txt")
    file_ket_qua = os.path.join(thu_muc, "OLop01_ket_qua.txt")
    tao_file_mau(ten_file)

    try:
        noi_dung = doc_file(ten_file)
        print("Noi dung file:")
        print(noi_dung)

        tong = tinh_tong(noi_dung)
        print("Tong cac so:", tong)

        ghi_file(file_ket_qua, noi_dung, tong)
        print("Da ghi ket qua vao file", file_ket_qua)

    except FileNotFoundError:
        print("Khong tim thay file")

    except ValueError:
        print("File chua du lieu khong phai so")


if __name__ == "__main__":
    main()