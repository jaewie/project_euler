isMultiple :: Int -> Int -> Bool
isMultiple num d = mod num d == 0

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

isPrime num = (num == 2) || (all (not . isMultiple num) [2..((isqrt num) + 1)])

primes :: [Int]
primes = filter (isPrime) [2..]

ans :: Int
ans = primes !! 10000
