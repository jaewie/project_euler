def get_num(x, y):
    if x == y:
        return x * 2 if x % 2 == 0 else x * 2 - 1
    elif x - y == 2:
        return 2 * (x - 1) if x % 2 == 0 else x * 2 - 3
    else:
        return None

N = int(raw_input())
for _ in xrange(N):
    x, y = map(int, raw_input().split(' '))
    value = get_num(x, y)
    if value is not None:
        print value
    else:
        print "No Number"
