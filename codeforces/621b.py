from collections import defaultdict


B = 999
TOP_LEFT = 0
TOP_RIGHT = 1


def combos(num):
    n = num - 1
    return n * (n + 1) / 2


n = int(raw_input())
bishops = {tuple(map(lambda x: int(x) - 1, raw_input().split())) for _ in range(n)}
counts = defaultdict(int)


for (r, c) in bishops:
    top_lx, top_ly = (r - min(r, c), c - min(r, c))
    top_rx, top_ry = (r - min(r, B - c), c + min(r, B - c))


    counts[top_lx, top_ly, TOP_LEFT] += 1
    counts[top_rx, top_ry, TOP_RIGHT] += 1


print sum(combos(c) for c in counts.values())
