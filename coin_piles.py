def coin_piles(a: int, b: int) -> None:
    """
    You have two coin piles containing a and b coins.
    On each move, one of two operation is possible:
    1) (a - 1) and (b - 2)
    2) (a - 2) and (b - 1)
    Your task is to efficiently find out if you can empty both the piles.

    Since we are subtracting 1 from a x number of times
    and 2 from b x number of times, it can be generalized.
        First operation:
            a - 1x = 0 -> a = x
            b - 2x = 0 -> b = 2x
            Equation 1 -> a + b = 3x
        Second operationg:
            a - 2y = 0 -> a = 2y
            b - 1y = 0 -> b = y
            Equation 2 -> a + b = 3y
        Equation 1 + Equation 2:
            2(a + b) = 6(x + y)
            a + b = 3(x + y)
            (a + b) / 3 = x + y
    Also if one pile is greater than twice the other pile, it cannot be emptied.
    """
    if (a > 2 * b) or (b > 2 * a):
        print("NO")
    elif (a + b) % 3 != 0:  # not divisible by 3
        print("NO")
    else:
        print("YES")


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        a, b = map(int, input().split())
        coin_piles(a, b)
