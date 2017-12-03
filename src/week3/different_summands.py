# Uses python3
"""
** Problem **
    Represent a given positive integer n as a sum of as many pairwise distinct
    positive integers as possible.

What is a greedy move and why is it a safe move?

"""
import sys


def optimal_summands(n):
    summands = []
    #write your code here
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
