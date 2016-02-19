'''
D[n, k] = # of ways to make change = n, using the first k coins

D[0, k] = 1 way to make change - n: empty set.
D[n, 0] = 0 ways to make change n if we can't use any coins.
D[n, k] = D[n, k - 1] + D[n - coins[k], k - 1].
          # ways to make without using kth coin + # ways to make with using kth coin
D[n, k] = 0 if n < 0

'''

def ways(N, ints):
    cache = {}

    for k in range(len(ints) + 1):
        cache[0, k] = 1

    for n in range(1, N + 1):
        cache[n, 0] = 0


    for n in range(1, N + 1):
        for k in range(1, len(ints) + 1):
            c = ints[k - 1]
            cache[n, k] = cache[n, k - 1]

            if n >= c:
                cache[n, k] += cache[n - c, k]

    return cache[N, len(ints)]

n, m = map(int, raw_input().split())
ints = map(int, raw_input().split())
print(ways(n, ints))
