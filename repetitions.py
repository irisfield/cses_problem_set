def repetitions(s: str) -> None:
    """
    A DNA sequence is a string consisting of characters: A, C, G, and T.
    Find the longest repetition in the sequence, where:
    1. The contiguous repetition of one character count as n sequences (e.g. AAA...n = n).
    2. The contiguous repetition of two characters count as one sequence (e.g. ACACAC...n = 1).
    """
    tmp = 0
    count = 0

    if len(set(s)) == 2:  # O(n)
        # contiguous repetition of two character count as 1 sequences
        count = 1
    else:
        # contiguous repetition of one character count as n sequences
        for i in range(len(s) - 1):  # O(n)
            if s[i] == s[i + 1]:
                # contiguous repetition of a character
                tmp += 1
            else:
                # the contiguity was interrupted, restart
                count = max(count, tmp + 1)
                tmp = 0  # reset the count
        count = max(count, tmp + 1)

    print(count)

if __name__ == "__main__":
    s = input()
    repetitions(s)  # O(n) + O(n) = O(n)
