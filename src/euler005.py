from collections import OrderedDict
from functools import reduce
from operator import mul


def smallest_multiple(n):
    factors = OrderedDict()
    for x in range(2, n + 1):
        for m in factors.keys():
            if x % m == 0:
                count = 0
                while x % m == 0:
                    count += 1
                    x //= m
                factors[m] = max(factors[m], count)
        if x > 1:
            factors[x] = 1
    return reduce(mul, [k ** v for k, v in factors.items()], 1)


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(smallest_multiple(n))
