import sys


def string_to_binary(s: str) -> str:
    """
    Chuyển từng ký tự trong s thành nhị phân 8 bit và nối lại thành chuỗi.
    """
    return ''.join(format(ord(ch), '08b') for ch in s)


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} \"message\"")
        sys.exit(1)

    message = sys.argv[1]
    binary_repr = string_to_binary(message)

    # Ghi chuỗi nhị phân vào file convert.txt
    with open("convert.txt", "w", encoding="utf-8") as f:
        f.write(binary_repr)

    # Ghi message gốc vào file message.txt
    with open("message.txt", "w", encoding="utf-8") as f:
        f.write(message)

    print("Đã ghi chuỗi nhị phân vào convert.txt")
    print("Đã ghi message gốc vào message.txt")


if __name__ == "__main__":
    main()

