# ==========================================
# Yêu cầu 1: Tạo file văn bản chứa các số thực
# ==========================================
def create_sample_file(filename):
    content = """10.5
20
-5.5
30
15.5
25"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)

    print(f"Đã tạo file dữ liệu mẫu: '{filename}'")
    print("-" * 50)


# ==========================================
# Yêu cầu 2 & 3: Đọc file, tìm max, min,
# tính trung bình và xử lý lỗi
# ==========================================
def calculate_statistics(filename):
    try:
        numbers = []

        with open(filename, "r", encoding="utf-8") as file:
            print(f"Đang đọc dữ liệu từ file '{filename}':")

            for line_number, line in enumerate(file, start=1):
                line = line.strip()

                # Bỏ qua dòng trống
                if not line:
                    continue

                try:
                    number = float(line)
                    numbers.append(number)

                except ValueError:
                    print(
                        f" -> Cảnh báo dòng {line_number}: "
                        f"'{line}' không phải số thực hợp lệ. Bỏ qua."
                    )

        # Kiểm tra file không có số
        if len(numbers) == 0:
            print("File không có số thực hợp lệ.")
            return

        maximum = max(numbers)
        minimum = min(numbers)
        average = sum(numbers) / len(numbers)

        print("-" * 50)
        print(f"Số lớn nhất: {maximum}")
        print(f"Số nhỏ nhất: {minimum}")
        print(f"Trung bình cộng: {average:.2f}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file '{filename}'.")

    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    input_file = "real_numbers.txt"

    # 1. Tạo file dữ liệu đầu vào
    create_sample_file(input_file)

    # 2. Tính max, min và trung bình
    calculate_statistics(input_file)


if __name__ == "__main__":
    main()