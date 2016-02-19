def solve(lst):
    d = {} # best value that can be reached with elements in the list 1...i inclusive
           # if we set the ith element as max, or min

    for i in range(1, len(lst)):
        for b in (True, False):
            val = lst[i] if b else 1
            if i == 1:
                  d[i, b] = max(abs(val - lst[i - 1]), abs(val - 1))
            else:
                prev_min_val = 1
                prev_max_val = lst[i - 1]

                d[i, b] = max(abs(val - prev_min_val) + d[i - 1, False],
                              abs(val - prev_max_val) + d[i - 1, True])

    return max(d[len(lst) - 1, False], d[len(lst) - 1, True])

T = int(raw_input())
for _ in range(T):
    _ = raw_input()
    lst = map(int, raw_input().split())
    print(solve(lst) if len(lst) > 1 else 0)
