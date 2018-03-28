"""Multiples of 3 and 5"""

from math import ceil


def alt_solution_1(n):
    """Find the sum of all multiples of 3 or 5 below `n`.

    This solution is slow.
    """
    x = 0
    total = 0
    while x < n:
        for d in [3, 2, 1, 3, 1, 2, 3]:
            x += d
            if x >= n:
                break
            total += x
    return total


def alt_solution_2(n):
    """Find the sum of all multiples of 3 or 5 below `n`.

    This solution is slow.
    """
    return (
        3 * sum(range(ceil(n / 3)))
        + 5 * sum(range(ceil(n / 5)))
        - 15 * sum(range(ceil(n / 15)))
    )


def multiples_of_3_and_5(n):
    """Find the sum of all multiples of 3 or 5 below `n`."""
    return (
        3 * ceil(n / 3) * (ceil(n / 3) - 1) // 2
        + 5 * ceil(n / 5) * (ceil(n / 5) - 1) // 2
        - 15 * ceil(n / 15) * (ceil(n / 15) - 1) // 2
    )


if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n = int(input())
        print(multiples_of_3_and_5(n))
