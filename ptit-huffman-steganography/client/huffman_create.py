import sys
from heapq import heappush, heappop, heapify
from collections import Counter, namedtuple
import unicodedata

class Node(namedtuple('Node', ['freq', 'char', 'left', 'right'])):
    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(text):
    freq_map = Counter(text)
    heap = [Node(freq, char, None, None) for char, freq in freq_map.items()]
    heapify(heap)
    while len(heap) > 1:
        node1 = heappop(heap)
        node2 = heappop(heap)
        merged = Node(node1.freq + node2.freq, None, node1, node2)
        heappush(heap, merged)
    return heap[0]


def build_codes(node, prefix='', code_map=None):
    if code_map is None:
        code_map = {}
    if node.char is not None:
        code_map[node.char] = prefix or '0'
    else:
        build_codes(node.left, prefix + '0', code_map)
        build_codes(node.right, prefix + '1', code_map)
    return code_map


def huffman_encode(text):
    root = build_huffman_tree(text)
    code_map = build_codes(root)
    encoded = ''.join(code_map[ch] for ch in text)
    return code_map, encoded


def remove_diacritics(s):
    """Chuyển chuỗi Unicode thành dạng không dấu"""
    normalized = unicodedata.normalize('NFKD', s)
    return ''.join(c for c in normalized if not unicodedata.combining(c))


def main(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

    # Chuyển sang không dấu
    text = remove_diacritics(text)
    # Loại bỏ dấu câu
    for punct in ['.', ',', '!', '?', ';', ':', '—', '–', '"', "'", '(', ')']:
        text = text.replace(punct, '')
    # Loại bỏ khoảng trắng, xuống dòng, tab
    text = text.replace(' ', '')
    text = text.replace('\n', '')
    text = text.replace('\t', '')

    code_map, encoded_text = huffman_encode(text)

    # Ghi bảng mã Huffman ra file huffman.txt
    try:
        with open('huffman.txt', 'w', encoding='utf-8') as out:
            for ch, code in sorted(code_map.items(), key=lambda x: (len(x[1]), x[1])):
                out.write(f"{ch}\t{code}\n")
        print("Bảng mã Huffman đã được lưu vào file 'huffman.txt'.")
    except IOError as e:
        print(f"Error khi ghi file: {e}")

    # In thông tin tóm tắt lên màn hình
    original_bits = len(text) * 8
    compressed_bits = len(encoded_text)
    ratio = compressed_bits / original_bits * 100
    print(f"Original size: {original_bits} bits")
    print(f"Compressed size: {compressed_bits} bits")
    print(f"Compression ratio: {ratio:.2f}%")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python huffman_file.py <path_to_text.txt>")
        sys.exit(1)
    main(sys.argv[1])
