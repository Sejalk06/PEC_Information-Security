"""Experiment 1: GCD/LCM using Euclid's algorithm and modular arithmetic."""

from math import gcd


def gcd_lcm():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    g = gcd(a, b)
    lcm = abs(a * b) // g if g else 0
    print(f"GCD = {g}")
    print(f"LCM = {lcm}")


def modular_operations():
    a = int(input("Enter first integer: "))
    b = int(input("Enter second integer: "))
    modulus = int(input("Enter positive modulus: "))
    if modulus <= 0:
        print("Modulus must be a positive integer.")
        return

    print("Addition:", (a + b) % modulus)
    print("Subtraction:", (a - b) % modulus)
    print("Multiplication:", (a * b) % modulus)
    if gcd(b, modulus) == 1:
        print("Division:", (a * pow(b, -1, modulus)) % modulus)
    else:
        print("Division: modular inverse of the second number does not exist.")


def main():
    print("1. GCD and LCM")
    print("2. Modular arithmetic (add, subtract, multiply, divide)")
    choice = input("Choose an option (1/2): ").strip()
    if choice == "1":
        gcd_lcm()
    elif choice == "2":
        modular_operations()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
