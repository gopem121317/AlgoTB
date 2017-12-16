# Uses python3
"""
** Problem **
    Represent a given positive integer n as a sum of as many pairwise distinct
    positive integers as possible.

What is a greedy move and why is it a safe move?

** Solution **

    To maximize a series of distinctive positive numbers that sum up to a given
    number, n, we naturally want to use AS SMALL AS POSSIBLE numbers first. So, we
    would pick 1 as the first number, and then reduce the problem to find the
    longest number list sum up to n-1, subjected to the constraint that 1 has
    been used. This process will continue until the required sum is less or
    equal to twice the smallest usable number, u, because the sum of the smallest
    2 usable integers (2u+1) is already greater than the requied sum.

    Recursively, we need to define a function that takes the requred sum n and
    the current smallest usable number u as two arguments, and return the
    remaining list of numbers. The break condition is when n<=2u, then the list
    will be just [n].

** Constraints in implementation **

    The length of the list goes as sqrt(n), when n~ 1E9, the length is ~1E5,
    which apparently exceeds the allowed depth of recursion in python. So, in
    the actual implementation, we do not explicitly use the recursive form of
    the function. Instead, we use a while loop to generate the numbers one by
    one. The spirit is exactly as the recursive approach described above.

"""
import sys

def next_number(n, u):
    """ return the first number in the remaining list of the numbers that sum
    up to n, with  the smallest number u
    """
    if n <= 2*u:
        return n
    else:
        return u


def optimal_summands(n):
    summands = []
    u=1
    while n>0:
        next_num = next_number(n,u)
        n = n - next_num
        u = u+1
        summands.append(next_num)

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    # test input for n
    #n=int(1e9)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
