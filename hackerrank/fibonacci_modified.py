a, b, n = map(int, raw_input().split())

for _ in range(n - 2):
    a, b = b, b ** 2 + a
print(b)
