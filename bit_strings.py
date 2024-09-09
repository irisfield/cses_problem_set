def bit_strings(n: int) -> None:
    """Your task is to calculate the number of bit strings of length n."""
    mod = 10**9 + 7
    num = int("1" * n, base=2) + 1  # O(n)
    print(num % mod)

if __name__ == "__main__":
    n = int(input())
    bit_strings(n)  # O(n)
