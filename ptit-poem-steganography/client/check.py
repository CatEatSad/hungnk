

import sys
import hashlib

EXPECTED_HASH = "ba17d699a58c66d270d3782fdc14ba57654df008419387876ab13d4bf9012ff6"


def sha256_hex(s: str) -> str:
    """Trả về chuỗi hex SHA-256 của s."""
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def main():
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <chuoi_can_kiem_tra>")
        sys.exit(1)

    candidate = sys.argv[1]
    candidate_hash = sha256_hex(candidate)

    if candidate_hash == EXPECTED_HASH:
        print("Correct secret")
    else:
        print("Wrong secret")
        print(f"  Chuỗi đã cho   : {candidate!r}")
        print(f"  SHA256 tính ra: {candidate_hash}")
        print(f"  SHA256 mong đợi: {EXPECTED_HASH}")


if __name__ == "__main__":
    main()
