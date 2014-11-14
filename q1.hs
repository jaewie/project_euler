isMultiple :: Int -> Int -> Bool
isMultiple num d = mod num d == 0

ans :: Int
ans = sum [x | x <- [1..1000], (isMultiple x 3) || (isMultiple x 5)]
