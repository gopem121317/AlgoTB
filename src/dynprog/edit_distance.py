# Uses python3
import numpy as np


def edit_distance(s, t):
    dist = np.zeros((len(s)+1, len(t)+1))
    dist[:, 0] = np.array(range(len(s) + 1))
    dist[0, :] = np.array(range(len(t) + 1))
    for j in range(1, len(t)+1):
        for i in range(1, len(s)+1):
            insertion = dist[i, j-1] + 1
            deletion = dist[i-1, j] + 1
            match = dist[i-1, j-1]
            mismatch = dist[i-1, j-1] + 1
            if s[i-1] == t[j-1]:
                dist[i, j] = min(insertion, deletion, match)
            else:
                dist[i, j] = min(insertion, deletion, mismatch)
    return int(dist[len(s), len(t)])


if __name__ == "__main__":
    print(edit_distance(input(), input()))
