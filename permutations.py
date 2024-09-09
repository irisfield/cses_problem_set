def permutations(n) -> None:
    """
    A permutation of integers 1,2,...,n is called beautiful
    if there are no adjacent elements whose difference is 1.
    """
    sol = ""

    if n == 2 or n == 3:
        sol = "NO SOLUTION"
    else:
        for i in range(2, n + 1, 2):  # O(n/2)
            sol += f"{i} "
        for i in range(1, n + 1, 2):  # O(n/2)
            sol += f"{i} "

    print(sol)

if __name__ == "__main__":
    n = int(input())
    permutations(n)  # O(n/2) * O(n/2) = O(n^2)
