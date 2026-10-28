"""Experiment 2: Caesar cipher and Playfair cipher (educational examples)."""


def caesar_cipher():
    text = input("Enter message: ")
    shift = int(input("Enter integer key/shift: ")) % 26

    def transform(message, amount):
        result = []
        for ch in message:
            if "A" <= ch <= "Z":
                result.append(chr((ord(ch) - ord("A") + amount) % 26 + ord("A")))
            elif "a" <= ch <= "z":
                result.append(chr((ord(ch) - ord("a") + amount) % 26 + ord("a")))
            else:
                result.append(ch)
        return "".join(result)

    encrypted = transform(text, shift)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", transform(encrypted, -shift))


def playfair_prepare(text):
    text = "".join(ch for ch in text.upper() if ch.isalpha()).replace("J", "I")
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        if i + 1 >= len(text):
            b = "X" if a != "X" else "Q"
            i += 1
        elif text[i + 1] == a:
            b = "X" if a != "X" else "Q"
            i += 1
        else:
            b = text[i + 1]
            i += 2
        pairs.append(a + b)
    return pairs


def playfair_cipher():
    key = input("Enter keyword: ").upper()
    message = input("Enter message (letters only are used): ").upper()
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    key_text = "".join(ch for ch in key if ch.isalpha()).replace("J", "I")
    sequence = []
    for ch in key_text + alphabet:
        if ch in alphabet and ch not in sequence:
            sequence.append(ch)
    grid = [sequence[i:i + 5] for i in range(0, 25, 5)]
    positions = {grid[r][c]: (r, c) for r in range(5) for c in range(5)}
    pairs = playfair_prepare(message)

    def transform_pair(pair, decrypt=False):
        a, b = pair
        ra, ca = positions[a]
        rb, cb = positions[b]
        step = -1 if decrypt else 1
        if ra == rb:
            return grid[ra][(ca + step) % 5] + grid[rb][(cb + step) % 5]
        if ca == cb:
            return grid[(ra + step) % 5][ca] + grid[(rb + step) % 5][cb]
        return grid[ra][cb] + grid[rb][ca]

    encrypted = "".join(transform_pair(pair) for pair in pairs)
    print("Key matrix:")
    for row in grid:
        print(" ".join(row))
    print("Prepared plaintext:", " ".join(pairs))
    print("Encrypted message:", encrypted)
    encrypted_pairs = [encrypted[i:i + 2] for i in range(0, len(encrypted), 2)]
    print("Decrypted prepared text:", "".join(transform_pair(pair, True) for pair in encrypted_pairs))
    print("Note: remove filler X/Q letters manually when restoring the original message.")


def main():
    print("1. Caesar cipher")
    print("2. Playfair cipher")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        caesar_cipher()
    elif choice == "2":
        playfair_cipher()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
