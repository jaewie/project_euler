import operator


def fact(n):
    return reduce(operator.mul, range(1, n + 1))


def sum_digits(num):
    digits = map(int, str(num))
    return sum(digits)

print(sum_digits(fact(100)))
