#Uses python3

import sys


def max_dot_product(a, b):
    #write your code here
    a_sorted = sorted(a)
    b_sorted = sorted(b)
    res = sum([x * y for x, y in zip(a_sorted, b_sorted)])
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
