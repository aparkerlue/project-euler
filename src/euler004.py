MIN_N = 10000


def largest_palindrome_prod_two_3digit_nos_lt(n):
    """Largest palindrome from product of two 3-digit numbers less than `n`."""
    n -= 1
    while n >= MIN_N:
        if str(n) == str(n)[::-1]:
            for i in range(100, 1000):
                if n % i == 0 and len(str(n // i)) == 3:
                    return n
        n -= 1
    return None


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(largest_palindrome_prod_two_3digit_nos_lt(n))
