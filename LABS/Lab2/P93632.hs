
eql :: [Int] -> [Int] -> Bool

eql x y = x == y

-------------------------------

prod :: [Int] -> Int

prod [] = 1
prod xs = foldl (*) 1 xs

-------------------------------

prodOfEvens :: [Int] -> Int

prodOfEvens [] = 1
prodOfEvens xs = foldl (*) 1 (filter even xs)

-------------------------------

powersOf2 :: [Int]

powersOf2 = iterate (*2) 1

-------------------------------

scalarProduct :: [Float] -> [Float] -> Float

scalarProduct x y = foldl (+) 0 (zipWith (*) x y)
