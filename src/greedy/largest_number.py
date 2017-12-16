# Uses python3
"""
** Problem **
    Construct the largest number with a set of positive integers

What is a greedy move and why is it a safe move?

"""
import sys


def is_greater_or_equal(a, b):
    return a + b >= b + a


def largest_number(numbers):
    res = ''
    while numbers:
        max_element = '0'
        for n in numbers:
            if is_greater_or_equal(n, max_element):
                max_element = n
        res += max_element
        numbers.remove(max_element)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
