def number_spiral(row: int, col: int) -> None:
    val = 0
    diag = lambda r, c: (r * c) - (c - 1)

    if row == col:
        val = diag(row, col)
    elif row > col:
        if row % 2 == 0:  # row is even
            val = diag(row, row) + (row - col)
        else:
            val = diag(row, row) - (row - col)
    else:
        if col % 2 == 0:
            val = diag(col, col) - (col - row)
        else:
            val = diag(col, col) + (col - row)

    print(val)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        r, c = map(int, input().split())
        number_spiral(r, c)  # O(1)
