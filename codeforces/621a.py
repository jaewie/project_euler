raw_input()
nums = map(int, raw_input().split())

total_all = sum(nums)
total_even = total_all if total_all % 2 == 0 else total_all - min(x for x in nums if x % 2)

print total_even
