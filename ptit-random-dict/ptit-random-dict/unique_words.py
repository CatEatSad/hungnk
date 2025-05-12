import re
from collections import Counter


def extract_unique_words(input_path='text.txt', output_path='unique_words.txt'):
    # Đọc toàn bộ nội dung file
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Chuyển về chữ thường và tách từ (loại bỏ dấu câu)
    # \w bao gồm cả chữ số và dấu gạch dưới; nếu bạn chỉ muốn chữ cái, thay \w bằng [a-zA-Z]
    words = re.findall(r'\b\w+\b', text.lower())

    # Đếm tần suất xuất hiện
    counts = Counter(words)

    # Lọc giữ các từ có count == 1
    unique_words = [word for word, cnt in counts.items() if cnt == 1]

    # Ghi kết quả ra file, mỗi từ trên một dòng
    with open(output_path, 'w', encoding='utf-8') as f:
        for word in unique_words:
            f.write(f"{word}\n")


if __name__ == '__main__':
    extract_unique_words()
