# ==========================================
# Yêu cầu 1: Thực hiện phép tính
# ==========================================
def calculate(number1, number2, operator):
    if operator == "+":
        return number1 + number2

    elif operator == "-":
        return number1 - number2

    elif operator == "*":
        return number1 * number2

    elif operator == "/":
        if number2 == 0:
            raise ZeroDivisionError
        return number1 / number2

    else:
        raise ValueError("Phép tính không hợp lệ")


# ==========================================
# Yêu cầu 2: Máy tính và xử lý lỗi
# ==========================================
def calculator():
    history_file = "history.txt"

    while True:
        print("\n========== MAY TINH ==========")
        print("1. Cong")
        print("2. Tru")
        print("3. Nhan")
        print("4. Chia")
        print("0. Thoat")
        print("==============================")

        choice = input("Nhap lua chon: ")

        if choice == "0":
            print("Ket thuc chuong trinh!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Lua chon khong hop le!")
            continue

        try:
            number1 = float(input("Nhap so thu nhat: "))
            number2 = float(input("Nhap so thu hai: "))

            if choice == "1":
                operator = "+"
            elif choice == "2":
                operator = "-"
            elif choice == "3":
                operator = "*"
            else:
                operator = "/"

            result = calculate(number1, number2, operator)

            print(f"Ket qua: {number1} {operator} {number2} = {result}")

            # Ghi phep tinh hop le vao file
            with open(history_file, "a", encoding="utf-8") as file:
                file.write(
                    f"{number1} {operator} {number2} = {result}\n"
                )

        except ValueError:
            print("Loi: Vui long nhap dung so!")

        except ZeroDivisionError:
            print("Loi: Khong the chia cho 0!")

        except Exception as e:
            print(f"Da xay ra loi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    calculator()


if __name__ == "__main__":
    main()