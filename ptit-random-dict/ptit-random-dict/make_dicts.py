import random
from collections import defaultdict


def load_words(path):
    """Đọc file mỗi dòng một từ, loại bỏ dòng rỗng."""
    with open(path, 'r', encoding='utf-8') as f:
        return [w.strip() for w in f if w.strip()]


def load_bitstring(path):
    """Đọc toàn bộ chuỗi bit (có thể nhiều dòng gộp lại)."""
    with open(path, 'r', encoding='utf-8') as f:
        data = f.read().strip().replace("\n", "")
    return data


def classify_full_stream(words, bitstring):
    """
    Duyệt toàn bộ chuỗi bit 2 bit một, ánh xạ lần lượt tới các từ (vòng qua danh sách khi hết).
    Thu thập tất cả các từ được ánh xạ vào từng nhóm unique.
    """
    n = len(words)
    pairs = [bitstring[i:i + 2] for i in range(0, len(bitstring) - len(bitstring) % 2, 2)]
    groups = defaultdict(list)

    for idx, code in enumerate(pairs):
        if code not in ('00', '01', '10', '11'):
            continue
        word = words[idx % n]
        # đưa từ vào nhóm nếu chưa có
        if word not in groups[code]:
            groups[code].append(word)
    # đảm bảo 4 nhóm luôn có key
    for c in ('00', '01', '10', '11'):
        groups.setdefault(c, [])
    return groups


def build_dict_sets(groups):
    """
    Tạo các bộ 4-từ sao cho:
    - Mỗi từ trong mỗi nhóm ít nhất xuất hiện một lần.
    - Không có bộ nào trùng lặp.
    """
    codes = ['00', '01', '10', '11']
    seen_quads = set()
    dict_sets = []
    # Đối với mỗi nhóm, với mỗi từ cần dùng ít nhất một lần
    for code in codes:
        for word in groups[code]:
            quad = [None] * 4
            quad[codes.index(code)] = word
            # chọn random từ cho các nhóm khác
            for other in codes:
                if other == code:
                    continue
                if not groups[other]:
                    raise ValueError(f"Nhóm {other} trống, không thể tạo bộ.")
                quad[codes.index(other)] = random.choice(groups[other])
            quad_tuple = tuple(quad)
            # đảm bảo không lặp lại
            attempts = 0
            while quad_tuple in seen_quads:
                for other in codes:
                    if other != code:
                        quad[codes.index(other)] = random.choice(groups[other])
                quad_tuple = tuple(quad)
                attempts += 1
                if attempts > 1000:
                    raise RuntimeError("Không thể sinh thêm tổ hợp độc nhất sau nhiều lần thử.")
            seen_quads.add(quad_tuple)
            dict_sets.append(list(quad_tuple))
    return dict_sets


def write_dict_file(dict_sets, out_path='dict.txt'):
    """Ghi mỗi bộ 4 từ ra một dòng, ngăn cách tab."""
    with open(out_path, 'w', encoding='utf-8') as f:
        for quad in dict_sets:
            f.write('\t'.join(quad) + '\n')
    print(f"Đã ghi {len(dict_sets)} bộ từ vào {out_path}")


def main():
    words_path = 'unique_words.txt'
    bits_path = 'convert.txt'
    output_path = 'dict.txt'

    words = load_words(words_path)
    bitstring = load_bitstring(bits_path)
    groups = classify_full_stream(words, bitstring)
    dict_sets = build_dict_sets(groups)
    write_dict_file(dict_sets, output_path)


if __name__ == '__main__':
    main()
