# ==========================================
# Yêu cầu 1: Tạo file văn bản mẫu
# ==========================================
def create_sample_file(filename):
    content = """Python la ngon ngu lap trinh.
Python rat de hoc.
Hoc Python can thuc hanh nhieu.
Python duoc su dung trong nhieu linh vuc."""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Da tao file du lieu mau: '{filename}'")
    print("-" * 50)


# ==========================================
# Yêu cầu 2 & 3: Đọc file, đếm từ và ghi kết quả
# ==========================================
def count_word(input_filename, output_filename):
    try:
        with open(input_filename, "r", encoding="utf-8") as file:
            noi_dung = file.read()

        tu_can_tim = input("Nhap tu can tim: ")

        so_lan = noi_dung.lower().split().count(tu_can_tim.lower())

        with open(output_filename, "w", encoding="utf-8") as file:
            file.write(f"Tu '{tu_can_tim}' xuat hien {so_lan} lan.")

        print("-" * 50)
        print(f"Tu '{tu_can_tim}' xuat hien {so_lan} lan.")
        print(f"Da ghi ket qua vao file '{output_filename}'.")

    except FileNotFoundError:
        print(f"Loi: Khong tim thay file '{input_filename}'.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    input_file = "OLop01_danh_sach_tu.txt"
    output_file = "word_count.txt"

    create_sample_file(input_file)
    count_word(input_file, output_file)


if __name__ == "__main__":
    main()