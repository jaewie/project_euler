n = int(raw_input())
plastic_cost = int(raw_input())
glass_cost = int(raw_input())
return_back = int(raw_input())

glass_real_cost = glass_cost - return_back
buys = 0


if n >= glass_cost and glass_real_cost < plastic_cost:
    buys += 1 + (n - glass_cost) / glass_real_cost
    n -= buys * glass_real_cost


buys += n / plastic_cost

print buys
