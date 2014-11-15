isMultiple :: Int -> Int -> Bool
isMultiple num d = mod num d == 0

isqrt :: Int -> Int
isqrt = floor . sqrt . fromIntegral

numMultiples :: Int -> Int
numMultiples 1 = 1
numMultiples num = 2 + foldr (\cur acc -> if isMultiple num cur then acc + 2 else acc) 0 [2..(isqrt num)]

triangleNumbers :: [Int]
triangleNumbers = [1] ++ zipWith (+) triangleNumbers [2..]

ans = head $ filter (\x -> numMultiples x > 500) triangleNumbers
