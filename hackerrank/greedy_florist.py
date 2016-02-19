_, k = map(int, raw_input().split())
numbers = sorted(map(int, raw_input().split()), reverse=True)

k_chunks = [numbers[i:i+k] for i in range(0, len(numbers), k)]
total = sum((i + 1) * sum(chunk) for i, chunk in enumerate(k_chunks))
print total
