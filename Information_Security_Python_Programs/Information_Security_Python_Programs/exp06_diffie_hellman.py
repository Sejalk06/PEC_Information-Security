"""Experiment 6: Diffie-Hellman shared-secret demonstration."""


def main():
    try:
        p = int(input("Enter a prime number p (small number for demo): "))
        g = int(input("Enter generator/base g: "))
        alice_private = int(input("Enter Alice's private integer: "))
        bob_private = int(input("Enter Bob's private integer: "))
    except ValueError:
        print("All inputs must be integers.")
        return

    if p <= 2 or not 1 < g < p or alice_private < 1 or bob_private < 1:
        print("Use p > 2, 1 < g < p, and positive private integers.")
        return

    alice_public = pow(g, alice_private, p)
    bob_public = pow(g, bob_private, p)
    alice_secret = pow(bob_public, alice_private, p)
    bob_secret = pow(alice_public, bob_private, p)

    print("Alice's public key =", alice_public)
    print("Bob's public key =", bob_public)
    print("Alice's shared secret =", alice_secret)
    print("Bob's shared secret =", bob_secret)
    print("Key exchange successful." if alice_secret == bob_secret else "Key exchange failed.")


if __name__ == "__main__":
    main()
