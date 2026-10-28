"""Experiment 8: Run basic GnuPG operations from Python.
Requires GnuPG installed and available as `gpg` on PATH.
This script lists keys and can encrypt/decrypt an existing text file.
"""

import shutil
import subprocess
from pathlib import Path


def run_gpg(args):
    result = subprocess.run(["gpg", *args], text=True, capture_output=True)
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="")
    if result.returncode != 0:
        print("GnuPG command failed with exit code", result.returncode)
    return result.returncode == 0


def main():
    if shutil.which("gpg") is None:
        print("GnuPG was not found. Install GnuPG and ensure `gpg` is on PATH.")
        print("Download: https://gnupg.org/download/")
        return

    print("1. List public keys")
    print("2. List secret/private keys")
    print("3. Encrypt a text file for a recipient")
    print("4. Decrypt an encrypted file")
    choice = input("Choose option (1-4): ").strip()

    if choice == "1":
        run_gpg(["--list-keys"])
    elif choice == "2":
        run_gpg(["--list-secret-keys"])
    elif choice == "3":
        source = Path(input("Input text file path: ").strip().strip('"'))
        recipient = input("Recipient email/key ID: ").strip()
        output = Path(input("Output encrypted file path (e.g. message.gpg): ").strip().strip('"'))
        if not source.is_file():
            print("Input file does not exist.")
            return
        run_gpg(["--output", str(output), "--encrypt", "--recipient", recipient, str(source)])
    elif choice == "4":
        source = Path(input("Encrypted file path: ").strip().strip('"'))
        output = Path(input("Output decrypted file path: ").strip().strip('"'))
        if not source.is_file():
            print("Encrypted file does not exist.")
            return
        run_gpg(["--output", str(output), "--decrypt", str(source)])
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
