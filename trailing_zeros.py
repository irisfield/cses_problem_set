def trailing_zeros(n: int) -> None:
    """
    Your task is to calculate the number of trailing zeros in the factorial n!.
    Pattern: The number of trailing zeros in n! is the number of 5's in n!
    """
    count = 0
    power_of_five = 5
    while power_of_five <= n:  # O(n)
        count += n // power_of_five
        power_of_five *= 5
    print(count)

if __name__ == "__main__":
    n = int(input())
    trailing_zeros(n)  # O(n)
