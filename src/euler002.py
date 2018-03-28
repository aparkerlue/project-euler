"""Even Fibonacci numbers"""


def even_fib(n):
    s = 0
    x, x_last = 1, 1
    while x < n:
        if x % 2 == 0:
            s += x
        x, x_last = x + x_last, x
    return s


if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        x = int(input())
        print(even_fib(x))
