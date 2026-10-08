import json


# ==========================================
# Yêu cầu 1: Tạo file config.json
# ==========================================
def create_config_file(filename):
    config = {
        "app_name": "MyApplication",
        "version": "1.0.0",
        "debug": True
    }

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(config, file, indent=4, ensure_ascii=False)

    print(f"Da tao file cau hinh: '{filename}'")
    print("-" * 50)


# ==========================================
# Yêu cầu 2 & 3: Đọc file JSON và hiển thị
# ==========================================
def read_config_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            config = json.load(file)

        # Dùng get() để lấy dữ liệu
        app_name = config.get("app_name", "Unknown")
        version = config.get("version", "Unknown")
        debug = config.get("debug", False)

        print("THONG TIN CAU HINH")
        print("-" * 30)
        print(f"Ten ung dung: {app_name}")
        print(f"Phien ban: {version}")
        print(f"Debug: {debug}")

    except FileNotFoundError:
        print(f"Loi: Khong tim thay file '{filename}'.")

    except json.JSONDecodeError:
        print(f"Loi: File '{filename}' khong dung dinh dang JSON.")

    except Exception as e:
        print(f"Da xay ra loi: {e}")


# ==========================================
# Chạy chương trình chính
# ==========================================
def main():
    config_file = "config.json"

    # Tao file JSON
    create_config_file(config_file)

    # Doc va hien thi file JSON
    read_config_file(config_file)


if __name__ == "__main__":
    main()