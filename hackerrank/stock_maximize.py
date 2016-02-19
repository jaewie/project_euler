# Buy on day i, if there's a day j > i s.t. price[j] > price[i]. Pick highest such price[j]
#
# So, for each day i, we need to find a max(lst[i + 1:])
#
# Keep an array maxar s.t. maxar[k] represents highest price number whose index is > k

def maximize(prices):
    maxar = [None] * len(prices)
    max_so_far = None
    for i in reversed(range(len(prices))):
        price = prices[i]
        if i == len(prices) - 1:
            max_so_far = price
        else:
            max_so_far = max(max_so_far, price)
        maxar[i] = max_so_far

    profit = 0

    for i, price_bought in enumerate(prices[:-1]):
        price_sold = maxar[i + 1]

        if price_sold > price_bought:
            profit += price_sold - price_bought
    return profit

T = int(raw_input())

for _ in range(T):
    _ = raw_input()
    prices = map(int, raw_input().split())
    print(maximize(prices))
