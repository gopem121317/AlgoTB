# Uses python3
"""Randomized Quick Sort with 3-way Partitions

"""
import sys
import random


def partition3(arr, l, r):
    x = arr[l]  # pivot element
    j, k = l, l  # j: final position of pivot element
                 # k: final position of last equal element
    for i in range(l+1, r+1):
        if arr[i] < x:
            j += 1
            k += 1
            # move to the 1st part
            arr[i], arr[k] = arr[k], arr[i]
            arr[j], arr[k] = arr[k], arr[j]
        elif arr[i] == x:  # equal element
            k += 1
            arr[i], arr[k] = arr[k], arr[i]  # move to the 2nd part
    arr[l], arr[j] = arr[j], arr[l]  # put pivot element to its final position
    return j, k


def partition2(arr, l, r):
    x = arr[l]
    j = l
    for i in range(l + 1, r + 1):
        if arr[i] <= x:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[l], arr[j] = arr[j], arr[l]
    return j


def randomized_quick_sort(arr, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    arr[l], arr[k] = arr[k], arr[l]
    # m = partition2(a, l, r)
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)
    m1, m2 = partition3(arr, l, r)
    randomized_quick_sort(arr, l, m1 - 1)
    randomized_quick_sort(arr, m2 + 1, r)


def _print_color(s):
    _COLOR_CODE = '7;31;43'
    print('\x1B[%sm' % _COLOR_CODE + s + '\x1B[0m')


def _stress_test(n_tests=10000):
    import numpy as np
    for _ in range(n_tests):
        arr_size = 10
        test_arr = np.random.randint(1, 1000, arr_size).tolist()
        # a.extend([99, 99])
        print('Original array: ')
        print(test_arr)
        randomized_quick_sort(test_arr, 0, arr_size - 1)
        try:
            assert test_arr == sorted(test_arr)
        except AssertionError:
            _print_color('Sorted array: WRONG!!')
            print(test_arr)
            break
        else:
            print('Sorted array: ')
            print(test_arr, '\n')


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # _stress_test()
