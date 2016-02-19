def max_val(nums):
    suffix_sum = {}
    for i in reversed(range(len(nums))):
        if i == len(nums) - 1:
            suffix_sum[i] = nums[i]
        else:
            suffix_sum[i] = nums[i] + suffix_sum[i + 1]


    cache = {}
    for i in reversed(range(len(nums))):
        num = nums[i]
        if i >= len(nums) - 3:
            cache[i] = sum(nums[i:])
        else:
            for j in range(1, 4):
                subtotal = suffix_sum[i + j] - cache[i + j]
                total = subtotal + sum(nums[i: i + j])
                cache[i] = max(total, cache.get(i, 0))


    return cache[0]


T = int(raw_input())

for _ in range(T):
    raw_input()
    nums = map(int, raw_input().split())
    print max_val(nums)
