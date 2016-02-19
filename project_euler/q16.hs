import Data.Char

ans = sum $ map (\c -> (ord c) - (ord '0')) $ show (2 ^ 1000)
