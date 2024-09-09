def two_sets(n: int) -> None:
    """
    Divide the numbers 1,2,...,n into two sets of equal sums,
    where the length of the two must equal to n.
    """
    riemann = lambda n: n * (n + 1) // 2
    rsum = riemann(n)  # O(1)
    if (rsum % 2 == 1):  # the sum of the numbers in the set is odd
        print("NO")
    else:
        set1 = set()
        set2 = set()
        set1str = ""
        set2str = ""
        set1sum = 0

        for i in range(n, 0, -1):  # O(n)
            if set1sum + i <= rsum // 2:
                set1.add(i)
                set1str += str(i) + " "
                set1sum += i
            else:
                set2.add(i)
                set2str += str(i) + " "

        print("YES")
        print(f"{len(set1)}\n{set1str}")
        print(f"{len(set2)}\n{set2str}")


if __name__ == "__main__":
    n = int(input())
    two_sets(n)  # O(n)
