# Uses python3
"""Implementing Binary Search

Implement the Binary Search Algorithm that allows searching very efficiently
(even huge) lists of positive integers, provided that the list is sorted.
Return the index of found element in the given array. If not found, return -1.
"""
import sys


def binary_search(a, x):
    if x < a[0] or x > a[-1]:
        return -1
    left, right = 0, len(a)
    while left <= right:
        mid = int(left + (right-left) / 2)
        if x == a[mid]:
            return mid
        elif x < a[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def linear_search(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1:n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end=' ')
