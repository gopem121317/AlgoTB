# Uses python3
"""Randomized Quick Sort with 3-way Partitions

"""
import sys
import random


def partition3(arr, l, r):
    x = arr[l]  # pivot element
    print('critical x: %d' % x)
    j, k = l, 0  # j: final position of pivot element
                 # k: number of equal elements
    for i in range(l+1, r+1):
        if arr[i] < x:  # same as 2-way partition
            j += 1
            arr[i], arr[j] = arr[j], arr[i]  # move to the 1st part
        elif arr[i] == x:  # equal element
            k += 1
            arr[i], arr[j + k] = arr[j + k], arr[i]  # move to the 2nd part
            print('equal elements swapped: ')
            print(arr)
    arr[l], arr[j] = arr[j], arr[l]  # put pivot element to its final position
    print('partially sorted: ')
    print(arr)
    return j, j+k


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
    print('random k: %d' % k)
    arr[l], arr[k] = arr[k], arr[l]
    # m = partition2(a, l, r)
    m1, m2 = partition3(arr, l, r)
    print('m1, m2: %d, %d' % (m1, m2))
    # randomized_quick_sort(a, l, m - 1)
    # randomized_quick_sort(a, m + 1, r)
    randomized_quick_sort(arr, l, m1 - 1)
    randomized_quick_sort(arr, m2 + 1, r)


def _print_color(s):
    _COLOR_CODE = '7;31;43'
    print('\x1B[%sm' % _COLOR_CODE + s + '\x1B[0m')


def _stress_test(n_tests=10000):
    import numpy as np
    for _ in range(n_tests):
        n = 10
        a = np.random.randint(1, 1000, n).tolist()
        print('Original array: ')
        print(a)
        randomized_quick_sort(a, 0, n - 1)
        try:
            assert a == sorted(a)
        except AssertionError:
            _print_color('Sorted array: WRONG!!!')
            print(a)
            break
        else:
            print('Sorted array: ')
            print(a, '\n')


if __name__ == '__main__':
    # input = sys.stdin.read()
    # n, *a = list(map(int, input.split()))
    a = [716, 883, 84, 353, 281, 873, 716, 590, 731, 229]
    n = len(a)
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
    # _stress_test()
