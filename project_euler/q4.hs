isPalindrome :: Int -> Bool
isPalindrome num = (show num) == (reverse $ show num)

ans :: Int
ans = maximum [x * y | x <- [999, 998..100], y <- [999, 998..100], isPalindrome (x * y)]
