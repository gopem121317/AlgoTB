# Uses python3
import sys


def optimal_sequence(n):
    numbers = list(range(1, n + 1))
    min_steps = list(range(n))
    min_steps[0] = 0
    prev_nums = [0]
    for i in range(1, n):
        m = numbers[i]
        if m % 3 == 0 and min_steps[m//3-1] <= min_steps[m//2-1]:
            min_steps[i] = min_steps[m//3-1] + 1
            prev_nums.append(m//3)
        elif m % 2 == 0 and min_steps[m//2-1] <= min_steps[i-1]:
            min_steps[i] = min_steps[m//2-1] + 1
            prev_nums.append(m//2)
        else:
            min_steps[i] = min_steps[i-1] + 1
            prev_nums.append(m-1)

    sequence = [n]
    j = n - 1
    while j > 0:
        prev = prev_nums[j]
        sequence.append(prev)
        j = prev - 1

    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
