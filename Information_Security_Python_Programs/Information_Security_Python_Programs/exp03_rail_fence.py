"""Experiment 3: Rail Fence transposition cipher."""


def encrypt(text, rails):
    if rails <= 1:
        return text
    rows = [""] * rails
    row, direction = 0, 1
    for ch in text:
        rows[row] += ch
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction
    return "".join(rows)


def decrypt(ciphertext, rails):
    if rails <= 1:
        return ciphertext
    pattern = []
    row, direction = 0, 1
    for _ in ciphertext:
        pattern.append(row)
        if row == 0:
            direction = 1
        elif row == rails - 1:
            direction = -1
        row += direction

    counts = [pattern.count(r) for r in range(rails)]
    rows = []
    offset = 0
    for count in counts:
        rows.append(list(ciphertext[offset:offset + count]))
        offset += count

    positions = [0] * rails
    output = []
    for r in pattern:
        output.append(rows[r][positions[r]])
        positions[r] += 1
    return "".join(output)


def main():
    text = input("Enter message: ")
    try:
        rails = int(input("Enter number of rails (at least 2): "))
    except ValueError:
        print("Please enter a valid integer.")
        return
    if rails < 2:
        print("Number of rails must be at least 2.")
        return
    encrypted = encrypt(text, rails)
    print("Encrypted message:", encrypted)
    print("Decrypted message:", decrypt(encrypted, rails))


if __name__ == "__main__":
    main()
