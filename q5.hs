isMultiple :: Int -> Int -> Bool
isMultiple num d = mod num d == 0

allMultiple :: Int -> Bool
allMultiple target = all (isMultiple target) [20,19..1]

ans :: Int
ans = head $ filter (allMultiple) [1..]
