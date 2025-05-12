import os
import sys

def format_size(size_bytes):
    """Chuyển đổi kích thước từ byte sang đơn vị phù hợp (KB, MB, GB)."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size_bytes < 1024:
            return f"{size_bytes:.2f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.2f} PB"

def compare_files(file1, file2):
    try:
        size1 = os.path.getsize(file1)
        size2 = os.path.getsize(file2)
    except FileNotFoundError as e:
        print(f"❌ Lỗi: {e}")
        sys.exit(1)

    print(f"📄 {file1}: {format_size(size1)}")
    print(f"📄 {file2}: {format_size(size2)}")

    diff = size2 - size1
    percent = (diff / size1) * 100 if size1 != 0 else 0

    if diff == 0:
        print("✅ Hai tệp có cùng kích thước.")
    elif diff > 0:
        print(f"📈 {file2} lớn hơn {file1} khoảng {format_size(diff)} ({percent:.2f}%)")
    else:
        print(f"📉 {file2} nhỏ hơn {file1} khoảng {format_size(-diff)} ({-percent:.2f}%)")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Cách sử dụng: python3 compare.py text.txt ste.txt")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
