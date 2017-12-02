# Uses python3
import sys


def gcd(a, b):
    if a <= b:
        small, big = a, b
    else:
        small, big = b, a

    while small != 0:
        small, big = big % small, small

    return big

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd(a, b))
