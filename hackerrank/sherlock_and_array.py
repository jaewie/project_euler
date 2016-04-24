def solve(lst):
    prefix_sums = get_prefix_sums(lst)
    suffix_sums = list(reversed(get_prefix_sums(reversed(lst))))

    for i in range(len(lst)):
        if i == 0:
            prefix_sum = 0
        else:
            prefix_sum = prefix_sums[i - 1]

        if i == len(lst) - 1:
            suffix_sum = 0
        else:
            suffix_sum = suffix_sums[i + 1]

        if prefix_sum == suffix_sum:
            return True

    return False


def get_prefix_sums(nums):
    prefix_sums = []
    for num in nums:
        if not prefix_sums:
            prefix_sums.append(num)
        else:
            prefix_sums.append(prefix_sums[-1] + num)
    return prefix_sums


N = int(raw_input())
for _ in range(N):
    raw_input()
    nums = map(int, raw_input().split(' '))
    if solve(nums):
        print 'YES'
    else:
        print 'NO'
