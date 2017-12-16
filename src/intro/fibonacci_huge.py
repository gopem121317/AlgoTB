# Uses python3
import sys


def get_fibonacci_modulo(n, m):
    if n <= 1:
        return n

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
    return period[idx]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(get_fibonacci_modulo(n, m))
