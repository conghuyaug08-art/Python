import csv


# ==========================================
# Yêu cầu 1: Nhập thông tin và ghi file CSV
# ==========================================
def create_contacts_file(filename):
    contacts = []

    while True:
        name = input("Nhap ten: ")
        phone = input("Nhap so dien thoai: ")

        if len(phone) == 10 and phone.isdigit():
            contacts.append([name, phone])
            break

        print("So dien thoai phai co dung 10 chu so!")

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Ghi dong tieu de
            writer.writerow(["Ho ten", "So dien thoai"])

            # Ghi thong tin
            for contact in contacts:
                writer.writerow(contact)

        print("-" * 50)
        print(f"Da ghi thong tin vao file '{filename}'.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")


# ==========================================
# Yêu cầu 2: Đọc và hiển thị file CSV
# ==========================================
def read_contacts_file(filename):
    try:
        with open(filename, "r", newline="", encoding="utf-8") as file:
            reader = csv.reader(file)

            print("\nDANH SACH LIEN HE")
            print("-" * 40)

            # Bo qua dong tieu de
            next(reader, None)

            for line_number, row in enumerate(reader, start=2):

                # Kiem tra thieu cot
                if len(row) < 2:
                    print(
                        f"Canh bao dong {line_number}: "
                        "Thieu thong tin."
                    )
                    continue

                print(f"Ho ten: {row[0]}")
                print(f"So dien thoai: {row[1]}")
                print("-" * 40)

    except FileNotFoundError:
        print(f"Loi: Khong tim thay file '{filename}'.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    contacts_file = "contacts.csv"

    # Tao file CSV
    create_contacts_file(contacts_file)

    # Doc va hien thi file CSV
    read_contacts_file(contacts_file)


if __name__ == "__main__":
    main()