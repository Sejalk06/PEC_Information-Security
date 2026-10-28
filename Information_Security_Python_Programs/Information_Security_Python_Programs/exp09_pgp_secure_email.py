"""Experiment 9: PGP-style signing, verification, encryption and decryption using GnuPG.
Requires GnuPG, a generated key pair, and a trusted recipient public key.
Use only keys/recipients you are authorized to use.
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
        print("Command failed with exit code", result.returncode)
    return result.returncode == 0


def main():
    if shutil.which("gpg") is None:
        print("GnuPG was not found. Install it and ensure `gpg` is on PATH.")
        print("Download: https://gnupg.org/download/")
        return

    print("1. Generate a personal key pair")
    print("2. Sign a file (detached signature)")
    print("3. Verify a detached signature")
    print("4. Sign and encrypt a file for a recipient")
    print("5. Decrypt and verify a signed/encrypted file")
    choice = input("Choose option (1-5): ").strip()

    if choice == "1":
        run_gpg(["--full-generate-key"])
    elif choice == "2":
        source = Path(input("File to sign: ").strip().strip('"'))
        if not source.is_file():
            print("File does not exist.")
            return
        run_gpg(["--armor", "--detach-sign", str(source)])
    elif choice == "3":
        source = Path(input("Original file path: ").strip().strip('"'))
        signature = Path(input("Signature file path (e.g. file.asc): ").strip().strip('"'))
        if not source.is_file() or not signature.is_file():
            print("Original file or signature file does not exist.")
            return
        run_gpg(["--verify", str(signature), str(source)])
    elif choice == "4":
        source = Path(input("File to sign and encrypt: ").strip().strip('"'))
        recipient = input("Recipient email/key ID: ").strip()
        output = Path(input("Output file (e.g. message.gpg): ").strip().strip('"'))
        if not source.is_file():
            print("File does not exist.")
            return
        run_gpg(["--armor", "--sign", "--encrypt", "--recipient", recipient,
                 "--output", str(output), str(source)])
    elif choice == "5":
        source = Path(input("Signed/encrypted file path: ").strip().strip('"'))
        output = Path(input("Output decrypted file path: ").strip().strip('"'))
        if not source.is_file():
            print("Input file does not exist.")
            return
        run_gpg(["--output", str(output), "--decrypt", str(source)])
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
