# Uses python3
def calc_fib(n):
    if n <= 1:
        return n
    fib = [0 for _ in range(n+1)]
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


n_in = int(input())
print(calc_fib(n_in))
