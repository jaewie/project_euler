fibs :: [Int]
fibs = [1, 2] ++ zipWith (+) fibs (tail fibs)

isEven :: Int -> Bool
isEven num = mod num 2 == 0

ans :: Int
ans = sum $ filter isEven $ takeWhile (\x -> x < 4000000) fibs
