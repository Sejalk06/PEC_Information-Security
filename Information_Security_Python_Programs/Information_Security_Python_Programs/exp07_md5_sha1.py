"""Experiment 7: MD5 and SHA-1 hash demonstrations. Not for modern security use."""

import hashlib


def main():
    message = input("Enter message to hash: ").encode("utf-8")
    print("MD5   :", hashlib.md5(message).hexdigest())
    print("SHA-1 :", hashlib.sha1(message).hexdigest())
    print("Note: MD5 and SHA-1 are outdated and unsuitable for security-sensitive use.")


if __name__ == "__main__":
    main()
