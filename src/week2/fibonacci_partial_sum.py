# Uses python3
import sys


def fibonacci_partial_sum(from_, to):
    from_ -= 1
    prev = 0
    curr = 1
    period = [0, 1]
    while True:
        prev, curr = curr, (prev + curr) % 10
        if prev == 0 and curr == 1:
            break
        period.append(curr)

    period.pop()
    lprd = len(period)
    id_fr = from_ % lprd
    id_to = to % lprd

    def csum_ld(n, idx):
        return (sum(period) * (n // lprd) + sum(period[:idx + 1])) % 10

    ld_fr = csum_ld(from_, id_fr)
    ld_to = csum_ld(to, id_to)

    return ld_to - ld_fr + 10 * (1 if ld_to < ld_fr else 0)


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum(from_, to))
