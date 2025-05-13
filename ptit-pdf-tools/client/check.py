

import sys
import hashlib

EXPECTED_HASH = "08aaff1d50fd2a74446c4497616882f7c362f380530d89d4144e3e0b007f6e5f"


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
