import re
import sys


def load_dictionary(dict_file):
    """Đọc dict.txt, trả về mapping từ từ (lowercase) -> mã 2-bit"""
    mapping = {}
    with open(dict_file, encoding='utf-8') as df:
        for line in df:
            parts = line.strip().split('\t')
            if len(parts) != 4:
                continue
            for bit, word in zip(['00', '01', '10', '11'], parts):
                mapping[word.lower()] = bit
    return mapping


def text_to_bits(text_file, dict_file):
    """Giải mã văn bản thành chuỗi bit dựa trên dict"""
    mapping = load_dictionary(dict_file)
    text = open(text_file, encoding='utf-8').read().lower()
    tokens = re.findall(r"\b\w+\b", text)
    return ''.join(mapping[t] for t in tokens if t in mapping)


def bits_to_string(bitstring):
    """Chuyển chuỗi bit thành chuỗi ký tự ASCII gốc"""
    # đảm bảo độ dài chia hết cho 8
    length = len(bitstring) - (len(bitstring) % 8)
    chars = [chr(int(bitstring[i:i + 8], 2)) for i in range(0, length, 8)]
    return ''.join(chars)


def main():
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <text_file> <dict_file> <output_text_file>")
        sys.exit(1)

    text_file, dict_file, out_text = sys.argv[1:4]
    # Bước 1: text -> bits
    bits = text_to_bits(text_file, dict_file)
    # Bước 2: bits -> original string
    message = bits_to_string(bits)

    with open(out_text, 'w', encoding='utf-8') as f:
        f.write(message)

    print(f"Recovered message written to '{out_text}' ({len(message)} characters)")


if __name__ == '__main__':
    main()
