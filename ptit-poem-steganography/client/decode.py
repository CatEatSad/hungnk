from typing import List

def poem_to_binary(poem: str) -> List[str]:
    """
    Chuyển mỗi dòng thơ thành một byte nhị phân.
    - poem: chuỗi nhiều dòng; các dòng rỗng ngăn cách giữa các khổ.
    Trả về danh sách các chuỗi 8-bit (ví dụ ['01101000', ...]).
    """
    bytes_out = []
    # Tách thành các dòng, loại bỏ dòng trắng dư
    lines = [ln.strip() for ln in poem.splitlines() if ln.strip()]
    for line in lines:
        bits = []
        # Tách từ (split mặc định theo whitespace)
        words = line.split()
        for w in words:
            # loại bỏ dấu câu hai đầu (nếu có)
            w_clean = w.strip('.,;?!—“”"\'')
            bits.append('1' if len(w_clean) % 2 else '0')
        # đảm bảo đủ 8 bit
        if len(bits) != 8:
            raise ValueError(f"Khổ thơ không có đúng 8 từ: {line!r}")
        bytes_out.append(''.join(bits))
    return bytes_out

def binary_to_text(bits_list: List[str]) -> str:
    """
    Giải mã danh sách chuỗi nhị phân 8-bit thành chuỗi văn bản.
    """
    chars = [chr(int(b, 2)) for b in bits_list]
    return ''.join(chars)

if __name__ == "__main__":
    # Bước 1: Đọc nội dung từ poem.txt
    with open("poem.txt", "r", encoding="utf-8") as file:
        poem_text = file.read()

    # Bước 2: Chuyển đổi thơ thành danh sách byte nhị phân
    binary_bytes = poem_to_binary(poem_text)

    # Bước 3: Ghi danh sách byte nhị phân vào bits.txt
    with open("bits.txt", "w", encoding="utf-8") as f:
        for b in binary_bytes:
            f.write(b + '\n')

    print("✅ Đã ghi bits.txt thành công.")
