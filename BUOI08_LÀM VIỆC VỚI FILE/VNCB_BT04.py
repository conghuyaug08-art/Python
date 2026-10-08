# ==========================================
# Yêu cầu 1: Tạo file nguồn mẫu
# ==========================================
def create_sample_file(filename):
    content = """Day la noi dung cua file nguon.
File nay dung de kiem tra chuc nang sao chep file.
Hoc Python can thuc hanh nhieu."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Da tao file mau: '{filename}'")
    print("-" * 50)


# ==========================================
# Yêu cầu 2 & 3: Sao chép file và xử lý lỗi
# ==========================================
def copy_file(source_filename, destination_filename):

    try:
        # Kiem tra hai file co trung ten hay khong
        if source_filename == destination_filename:
            print("Loi: File nguon va file dich khong duoc trung ten!")
            return

        # Mo file nguon de doc
        with open(source_filename, "r", encoding="utf-8") as source_file:

            # Mo file dich de ghi
            with open(destination_filename, "w", encoding="utf-8") as destination_file:

                for line in source_file:
                    destination_file.write(line)

        print("-" * 50)
        print(f"Sao chep thanh cong!")
        print(f"File nguon: {source_filename}")
        print(f"File dich: {destination_filename}")

    except FileNotFoundError:
        print(f"Loi: Khong tim thay file nguon '{source_filename}'.")

    except PermissionError:
        print("Loi: Khong co quyen truy cap file.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")

    finally:
        print("-" * 50)
        print("Ket thuc qua trinh sao chep file.")


# ==========================================
# Chay chuong trinh chinh
# ==========================================
def main():
    source_file = "source.txt"
    destination_file = "copy.txt"

    # Tao file nguon mau
    create_sample_file(source_file)

    # Nhap ten file dich
    destination_file = input("Nhap ten file dich: ")

    # Sao chep file
    copy_file(source_file, destination_file)


if __name__ == "__main__":
    main()