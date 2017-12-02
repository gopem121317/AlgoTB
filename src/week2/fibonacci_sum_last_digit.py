# Uses python3
import sys


def get_fibonacci_modulo(n, m):
    prev = 0
    curr = 1
    period = [0, 1]
    while True:
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            break
        period.append(curr)

    period.pop()
    len_prd = len(period)
    idx = n % len_prd
    return period, len_prd, idx


def fibonacci_sum(n):
    prd, l, idx = get_fibonacci_modulo(n, 10)
    return (sum(prd) * (n // l) + sum(prd[:idx+1])) % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum(n))
