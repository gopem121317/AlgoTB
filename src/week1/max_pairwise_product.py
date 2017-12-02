# python3
n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

# result = 0
# for i in range(0, n):
    # for j in range(i+1, n):
        # if a[i]*a[j] > result:
            # result = a[i]*a[j]

a1 = max(a)
a.remove(a1)
a2 = max(a)
result = a1 * a2
print(result)
