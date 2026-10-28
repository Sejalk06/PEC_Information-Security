# Information Security Practical Programs (Python)

This folder contains separate Python files for all 10 experiments in the supplied Information Security syllabus.

## Files

1. `exp01_gcd_lcm_modular.py` — GCD/LCM and modular arithmetic menu
2. `exp02_caesar_playfair.py` — Caesar and Playfair cipher menu
3. `exp03_rail_fence.py` — Rail Fence encryption/decryption
4. `exp04_des_single_round.py` — One standard DES round, including round-1 key generation
5. `exp05_rsa.py` — RSA key calculation and numeric message encryption/decryption
6. `exp06_diffie_hellman.py` — Diffie–Hellman shared-secret demonstration
7. `exp07_md5_sha1.py` — MD5 and SHA-1 hash outputs
8. `exp08_gnupg_operations.py` — Python helper for GnuPG key listing, encryption and decryption
9. `exp09_pgp_secure_email.py` — Python helper for GnuPG signing, verification, encryption and decryption
10. `exp10_wireshark_pcap_analysis.py` — Offline packet-capture analysis using Scapy

## Run on Windows / VS Code

1. Extract the ZIP file.
2. Open the extracted folder in VS Code.
3. Open Terminal > New Terminal.
4. Run any file, for example:

   ```powershell
   python exp01_gcd_lcm_modular.py
   ```

Use `python filename.py` for any other file.

## Dependencies / tools

- Experiments 1–7: Python 3.8+; no third-party packages required.
- Experiments 8–9: Install GnuPG and make sure the `gpg` command is available in PATH. These scripts call the GnuPG command-line tool; they do not implement the OpenPGP cryptographic format themselves.
- Experiment 10: Install Scapy using `python -m pip install scapy`. First capture traffic in Wireshark and save a `.pcap` or `.pcapng` file, then point the Python script to it.

## Suggested quick tests

- Experiment 1: choose GCD/LCM; enter `12` and `18`; expect GCD `6`, LCM `36`.
- Experiment 2: choose Caesar; enter `HELLO`, shift `3`; expect `KHOOR`, then `HELLO`.
- Experiment 3: message `WEAREDISCOVERED`, rails `3`; decrypted output should match the original.
- Experiment 4: plaintext `0123456789ABCDEF`, key `133457799BBCDFF1`; the first round key should be `1B02EFFC7072`.
- Experiment 5: p `5`, q `11`, message `9`; decrypted message should be `9`.
- Experiment 6: p `23`, g `5`, Alice private `6`, Bob private `15`; both shared secrets should match.
- Experiment 7: message `abc`; MD5 should be `900150983cd24fb0d6963f7d28e17f72`, SHA-1 should be `a9993e364706816aba3e25717850c26c9cd0d89d`.

## Important notes

- These are educational demonstrations, not production cryptography.
- DES, MD5 and SHA-1 are obsolete for modern security-sensitive use.
- RSA here uses small demonstration primes and is not secure for real data.
- Diffie–Hellman inputs must be appropriate for a real cryptographic group; the small values used in practicals are for learning only.
- GnuPG and Wireshark practicals may require external tools, keys, permissions, and a capture file. They cannot produce meaningful results without those prerequisites.
- Your syllabus says “any one” for Experiments 1, 2, 3, and 7. Confirm with your instructor whether to submit one alternative or both.
