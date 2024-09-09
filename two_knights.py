def two_knights(n: int) -> None:
    """
    On an n x n chessboard, the total number of ways to place:
    1. The first random piece is n^2.
    2. The second random piece (without double counting) is n^2(n^2 - 1) / 2.

    A knight can only move in an L-shape, either 2x1 or 1x2.
    The second knight cannot be placed anywhere within a 2x3 or 3x2 square of the first one.
    Otherwise, they can attack each other.

    3. The number of 2x3 rectables on an n x n board is (n - 2)(n - 1)
    4. The number of 3x2 rectables on an n x n board is (n - 1)(n - 2)
    5. The combination of these two numbers is 4(n - 2)(n - 1).

    """
    total = lambda n: n**2 * (n**2 - 1) // 2
    danger_square = lambda n: 4 * (n - 2) * (n - 1)

    for k in range(1, n + 1):
        print(total(k) - danger_square(k))

if __name__ == "__main__":
    n = int(input())
    two_knights(n)  # O(1)
