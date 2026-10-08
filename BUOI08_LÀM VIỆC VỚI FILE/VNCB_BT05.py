# ==========================================
# Yêu cầu 1: Nhập số lượng phần tử
# ==========================================
def input_number():
    while True:
        try:
            n = int(input("Nhap so luong so nguyen: "))

            if n > 0:
                return n

            print("So luong phai lon hon 0!")

        except ValueError:
            print("Loi: Vui long nhap mot so nguyen!")


# ==========================================
# Yêu cầu 2: Nhập danh sách và ghi vào file
# ==========================================
def create_integer_file(filename, n):
    numbers = []

    for i in range(n):
        while True:
            try:
                number = int(input(f"Nhap so nguyen thu {i + 1}: "))
                numbers.append(number)
                break

            except ValueError:
                print("Loi: Vui long nhap dung so nguyen!")

    try:
        with open(filename, "w", encoding="utf-8") as file:
            for number in numbers:
                file.write(f"{number}\n")

        print("-" * 50)
        print(f"Da ghi {n} so nguyen vao file '{filename}'.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    output_file = "integers.txt"

    # Nhap so luong phan tu
    n = input_number()

    # Nhap danh sach va ghi file
    create_integer_file(output_file, n)


if __name__ == "__main__":
    main()