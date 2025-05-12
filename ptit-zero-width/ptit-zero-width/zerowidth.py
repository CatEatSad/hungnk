def text_to_bits(text: str, encoding='utf-8', errors='surrogatepass') -> str:
    data = text.encode(encoding, errors)
    return ''.join(f"{byte:08b}" for byte in data)


def hide_zero_width(cover_text: str, secret: str) -> str:
    bits = text_to_bits(secret)
    zw = '\u200b'
    result = []
    bit_idx = 0

    for ch in cover_text:
        if ch == ' ' and bit_idx < len(bits):
            b = bits[bit_idx]
            if b == '0':
                result.append(' ' + zw)
            else:
                result.append(zw + ' ')
            bit_idx += 1
        else:
            result.append(ch)

    if bit_idx < len(bits):
        raise ValueError("Cover text không đủ số dấu cách để giấu hết thông điệp.")

    return ''.join(result)


if __name__ == "__main__":
    # Đọc văn bản gốc từ file
    with open('text.txt', 'r', encoding='utf-8') as f:
        cover = f.read()

    # Đọc chuỗi bí mật từ file
    with open('secret.txt', 'r', encoding='utf-8') as f:
        secret = f.read().strip()

    # Mã hóa
    stego = hide_zero_width(cover, secret)

    # Ghi ra file kết quả
    with open('output.txt', 'w', encoding='utf-8') as f:
        f.write(stego)

    print("✅ Đã giấu thông điệp và lưu vào 'output.txt'")
