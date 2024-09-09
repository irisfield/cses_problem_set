def weird_algorithm(n: int) -> None:
    """Collatz conjecture, also known as the 3n + 1 conjecture."""
    output = [n]
    while n > 1:
        n = (n // 2) if (n % 2 == 0) else (3 * n + 1)
        output.append(n)
    print(*output)

if __name__ == "__main__":
    n = int(input())
    weird_algorithm(n)
