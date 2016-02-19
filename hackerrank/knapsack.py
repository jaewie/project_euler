def closest(nums, target):
    d = {0}
    last_t = 0
    for t in range(target + 1):
        for num in nums:
            if t - num in d:
                d.add(t)
                last_t = t
    return last_t

test_cases = int(raw_input())
for _ in range(test_cases):
    _, target = map(int, raw_input().split())
    nums = map(int, raw_input().split())

    print(closest(nums, target))
