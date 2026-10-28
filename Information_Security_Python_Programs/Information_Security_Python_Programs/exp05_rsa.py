"""Experiment 5: Educational RSA encryption and decryption."""

from math import gcd


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def main():
    try:
        p = int(input("Enter first prime number p: "))
        q = int(input("Enter second prime number q: "))
    except ValueError:
        print("Please enter integers.")
        return
    if p == q or not is_prime(p) or not is_prime(q):
        print("Please enter two different prime numbers.")
        return

    n = p * q
    phi = (p - 1) * (q - 1)
    e = 2
    while e < phi and gcd(e, phi) != 1:
        e += 1
    if e >= phi:
        print("Could not find a valid public exponent.")
        return
    d = pow(e, -1, phi)

    try:
        message = int(input(f"Enter a message number from 0 to {n - 1}: "))
    except ValueError:
        print("Message must be an integer.")
        return
    if not 0 <= message < n:
        print("Message must be between 0 and n-1.")
        return

    encrypted = pow(message, e, n)
    decrypted = pow(encrypted, d, n)
    print("n =", n)
    print("phi(n) =", phi)
    print("Public key (e, n) =", (e, n))
    print("Private key (d, n) =", (d, n))
    print("Encrypted message =", encrypted)
    print("Decrypted message =", decrypted)


if __name__ == "__main__":
    main()
