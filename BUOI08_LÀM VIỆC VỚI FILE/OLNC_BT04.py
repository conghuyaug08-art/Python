
import csv
import os


def tao_file_mau(ten_file):
    with open(ten_file, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ma", "ten", "gia", "so_luong"])
        writer.writerow(["SP01", "Ban phim", 200000, 5])
        writer.writerow(["SP02", "Chuot", 150000, 15])
        writer.writerow(["SP03", "Tai nghe", 300000, 8])


def doc_csv(ten_file):
    with open(ten_file, "r", encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f))


def cap_nhat_gia(ds_san_pham):
    for sp in ds_san_pham:
        try:
            gia = float(sp["gia"])
            so_luong = int(sp["so_luong"])

            if gia < 0 or so_luong < 0:
                raise ValueError

            if so_luong < 10:
                gia *= 1.05

            sp["gia"] = round(gia, 2)

        except ValueError:
            print("Du lieu gia hoac so luong khong hop le:", sp)
            raise

    return ds_san_pham


def ghi_csv(ten_file, ds_san_pham):
    with open(ten_file, "w", encoding="utf-8", newline="") as f:
        fieldnames = ["ma", "ten", "gia", "so_luong"]
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(ds_san_pham)


def main():
    thu_muc = os.path.dirname(os.path.abspath(__file__))

    file_goc = os.path.join(thu_muc, "products.csv")
    file_moi = os.path.join(thu_muc, "products_new.csv")

    tao_file_mau(file_goc)

    try:
        ds_san_pham = doc_csv(file_goc)
        ds_san_pham = cap_nhat_gia(ds_san_pham)
        ghi_csv(file_moi, ds_san_pham)

        print("Cap nhat thanh cong!")
        print("Du lieu moi:")

        for sp in ds_san_pham:
            print(sp)

        print("Da ghi vao products_new.csv")

    except FileNotFoundError:
        print("Khong tim thay file CSV")

    except ValueError:
        print("Gia hoac so luong phai la so hop le")


if __name__ == "__main__":
    main()
