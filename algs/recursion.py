def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def collatz(n: int) -> int:
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + collatz(n / 2)
    else:
        return 1 + collatz(3 * n + 1)


if __name__ == "__main__":
    n = 4
    steps = collatz(n)
    print(f"Number: {n}; Steps: {steps}")

    n = 567
    steps = collatz(n)
    print(f"Number: {n}; Steps: {steps}")

    n = 1
    steps = collatz(n)
    print(f"Number: {n}; Steps: {steps}")

    n = 3214324
    steps = collatz(n)
    print(f"Number: {n}; Steps: {steps}")