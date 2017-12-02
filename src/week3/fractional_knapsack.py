# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    loot = list()
    pr = [v / w for v, w in zip(values, weights)]
    sorte_items = sorted(zip(pr, values, weights), key=lambda x: x[0], reverse=True)
    for p, v, w in sorte_items:
        if capacity >= w:
            value += v
            loot.append([p, w])
            capacity -= w
        else:
            value += p * capacity
            loot.append([p, capacity])
            capacity = 0
            break
    # print(loot)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
