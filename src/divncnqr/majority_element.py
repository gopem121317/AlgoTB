# Uses python3
"""Finding a Majority Element

Find the majority of a sequence of elements (positive integers).
Majority means the number of an element is greater than 1/2 of the
total number of elements in the given array.
If majority found, return 1, o/w return 0.
"""
import sys


def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    # write your code here
    distinct_elements = {}
    for x in a:
        if x in distinct_elements;


    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
