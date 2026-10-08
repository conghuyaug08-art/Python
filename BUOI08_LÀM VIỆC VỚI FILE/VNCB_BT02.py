# ==========================================
# Yêu cầu 1: Tạo file văn bản chứa các số
# ==========================================
def create_sample_file(filename):
    content = """10
25

-5
abc
100
45.5
20
17
8"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Đã tạo file dữ liệu mẫu: '{filename}'")
    print("-" * 50)


# ==========================================
# Yêu cầu 2 & 3: Đọc file, tách số chẵn/lẻ
# và xử lý dữ liệu không hợp lệ
# ==========================================
def separate_even_odd(input_filename, even_filename, odd_filename):
    try:
        with open(input_filename, "r", encoding="utf-8") as infile, \
             open(even_filename, "w", encoding="utf-8") as even_file, \
             open(odd_filename, "w", encoding="utf-8") as odd_file:

            print(f"Đang đọc dữ liệu từ file '{input_filename}':")

            for line_number, line in enumerate(infile, start=1):
                line = line.strip()

                # Bỏ qua dòng trống
                if not line:
                    continue

                try:
                    number = int(line)

                    if number % 2 == 0:
                        even_file.write(f"{number}\n")
                    else:
                        odd_file.write(f"{number}\n")

                except ValueError:
                    print(
                        f" -> Cảnh báo dòng {line_number}: "
                        f"'{line}' không phải số nguyên hợp lệ. Bỏ qua."
                    )

        print("-" * 50)
        print(f"Đã ghi số chẵn vào file '{even_filename}'.")
        print(f"Đã ghi số lẻ vào file '{odd_filename}'.")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{input_filename}'.")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    input_file = "numbers.txt"
    even_file = "even.txt"
    odd_file = "odd.txt"

    # 1. Tạo file dữ liệu đầu vào
    create_sample_file(input_file)

    # 2. Tách số chẵn và số lẻ
    separate_even_odd(input_file, even_file, odd_file)


if __name__ == "__main__":
    main()