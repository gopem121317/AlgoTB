# Uses python3
import sys
import numpy as np


def optimal_weight(W, w):
    w = sorted(w)
    value = np.zeros((W+1, len(w)+1))
    for j in range(1, len(w)+1):
        for i in range(1, W+1):
            value[i, j] = value[i, j-1]
            if w[j-1] <= i:
                val = value[i-w[j-1], j-1] + w[j-1]
                if value[i, j] < val:
                    value[i, j] = val
    return int(value[W, len(w)])


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
