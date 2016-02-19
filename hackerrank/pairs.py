from collections import Counter

n, k = map(int, raw_input().split())
lst = map(int, raw_input().split())
counter = Counter(lst)
total = 0

for key, val in counter.items():
    if key - k in counter:
        total += val * counter[key - k]
print total
