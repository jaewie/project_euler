def adj(N, K):
    cache = {}

    for n in range(0, N + 1):
        for k in range(0, n + 1):
            for last_bit_one in (False, True):
                key = (n, k, last_bit_one)
                if n == k == 0:
                    cache[key] = 1
                elif k == 0:
                    if last_bit_one:
                        cache[key] = cache[(n - 1, k, False)]
                    else:
                        cache[key] = cache[(n - 1, k, True)] + cache[(n - 1, k, False)]
                elif n == k:
                    cache[key] = 1 if last_bit_one else 0
                else:
                    if last_bit_one:
                        cache[key] = cache[(n - 1, k, False)] + cache[(n - 1, k - 1, True)]
                    else:
                        cache[key] = cache[(n - 1, k, False)] + cache[(n - 1, k, True)]
    return cache

cache = adj(100, 100)
N = int(raw_input())

for _ in xrange(N):
    x, y, z = map(int, raw_input().split(' '))
    print x, cache[y, z, False]
