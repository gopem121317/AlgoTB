# Uses python3
import sys


def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    prev = 0
    curr = 1

    for _ in range(n - 1):
        prev, curr = curr, (prev + curr) % 10

    return curr

if __name__ == '__main__':
    n_in = sys.stdin.read()
    n_in_int = int(n_in)
    print(get_fibonacci_last_digit(n_in_int))
