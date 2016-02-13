def divisor_sum(num):
    return 1 + sum(i + num / i for i in range(2, int(num ** 0.5) + 1)
                   if num % i == 0)


def amicable_nums(num):
    d = {i: divisor_sum(i) for i in range(2, num + 1)}
    return sum(a for a, b in d.iteritems() if a != b and b < num and d.get(b) == a)


print amicable_nums(10000)
