# Uses python3
import sys

COINS = [10, 5, 1]


def get_change(m):
    ttl = 0
    chgs = dict()
    while m > 0:
        for c in COINS:
            if m >= c:
                n = m // c
                m -= n * c
                chgs[c] = n
                ttl += n
    # print(chgs)
    return ttl


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
