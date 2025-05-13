from typing import List

def binary_to_text(bits_list: List[str]) -> str:
    """
    Giải mã danh sách chuỗi nhị phân 8-bit thành chuỗi văn bản.
    """
    chars = [chr(int(b, 2)) for b in bits_list]
    return ''.join(chars)

if __name__ == "__main__":
    try:
        with open("bits.txt", "r", encoding="utf-8") as f:
            bits_from_file = [line.strip() for line in f if line.strip()]

        decoded_text = binary_to_text(bits_from_file)

        print("🔓 Văn bản giải mã từ bits.txt:")
        print(decoded_text)
    except FileNotFoundError:
        print("❌ Tệp 'bits.txt' không tồn tại.")
    except ValueError as e:
        print(f"❌ Lỗi khi giải mã: {e}")
