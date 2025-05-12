

import sys
import hashlib

EXPECTED_HASH = "fe5db072b18dd3b5c8d7435b5fc3578127b961a928f33bed9a0532ccc9023fb4"


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
