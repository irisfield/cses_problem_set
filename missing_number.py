def missing_number(n: int, ln: list[int]) -> None:
    """
    Each number in ln is distinct and between 1 and n (inclusive).
    EDGE CASES:
    1. The missing number is 1.
    2. The missing number is n.
    """
    ln = sorted(ln)  # O(n*log(n))
    missing = None

    if ln[0] > 1:  # the missing number is 1
        missing = 1
    elif ln[-1] < n:  # the missing number is n
        missing = n
    else:  # the missing number is in between 1 and n
        for i in range(len(ln) - 1):  # O(n)
            if (ln[i + 1] - ln[i] > 1):
                missing = ln[i] + 1

    print(missing)

if __name__ == "__main__":
    n = int(input())
    ln = [int(x) for x in input().split()]
    missing_number(n, ln)  # O(n*log(n))
