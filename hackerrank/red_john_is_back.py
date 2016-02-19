def ways(cols, rows=4):
    cache = {0: 1}

    for col in range(1, cols + 1):
        vertical_count =  cache[col - 1]
        horizontal_count = cache.get(col - 4, 0)
        cache[col] = vertical_count + horizontal_count
    return cache

def primes(upto):
    candidates = [True for _ in xrange(upto + 1)]
    candidates[0] = False
    candidates[1] = False
    i = 2

    while i < len(candidates):
        fst = candidates[i]
        if fst:
            for c in xrange(i + i, upto + 1, i):
                candidates[c] = False
        i += 1
    return candidates

T = int(raw_input())
jobs = [int(raw_input()) for _ in range(T)]
max_job = max(jobs)

cache = ways(max_job, 4)
num_ways = map(lambda cols: cache[cols], jobs)

primes_max = [i for i, b in enumerate(primes(max(num_ways))) if b]
for num in num_ways:
    count = len(filter(lambda x: x <= num, primes_max))
    print(count)
