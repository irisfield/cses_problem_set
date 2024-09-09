def increasing_array(n: int, ln: list[int]) -> None:
    """
    You are given an array of n integers.
    You want to modify the array so that it is increasing,
    i.e., every element is at least as large as the previous element.
    What is the minimum number of moves required to make the array strictly increasing?
    """
    total = 0

    for i in range(1, n):  # O(n)
        if ln[i - 1] > ln[i]:
            total += ln[i - 1] - ln[i]
            ln[i] = ln[i - 1]

    print(total)

if __name__ == "__main__":
    n = int(input())
    ln = [int(x) for x in input().split()]
    increasing_array(n, ln)  # O(n)
