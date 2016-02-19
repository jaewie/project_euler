isMultiple :: Int -> Int -> Bool
isMultiple num d = mod num d == 0

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

isPrime num = (num == 2) || (all (not . isMultiple num) [2..((isqrt num) + 1)])

allFactorsLessThanSqrt :: Int -> [Int]
allFactorsLessThanSqrt target  = filter (isMultiple target) [2..((isqrt target) + 1)]

largestPrimeFactor :: Int -> Int
largestPrimeFactor num = head $ filter (isPrime) $ reverse $ allFactorsLessThanSqrt num
