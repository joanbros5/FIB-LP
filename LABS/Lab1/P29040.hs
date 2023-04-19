insert :: [Int] -> Int -> [Int]

insert [] y = [y]
insert (x:xs) y
    | y <= x = y : x : xs
    | otherwise = x : insert xs y


isort :: [Int] -> [Int]

isort [] = []
isort (x:xs) = insert (isort xs) x

-------------------------------

remove :: [Int] -> Int -> [Int]

remove [] _ = []
remove (x:xs) y
    | y == x = xs
    | otherwise = x : remove xs y

ssort :: [Int] -> [Int]

ssort [] = []
ssort llista = min : ssort (remove llista min)
    where
        min = minimum llista

-------------------------------

merge :: [Int] -> [Int] -> [Int]

merge [] xs = xs
merge xs [] = xs
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

msort :: [Int] -> [Int]

msort [] = []
msort [x] = [x]
msort xs = merge (msort l) (msort r)
    where
        l = take (div (length xs) 2 ) xs
        r = drop (div (length xs) 2 ) xs

-------------------------------

--qsort :: [Int] -> [Int]


-------------------------------

--genQsort :: Ord a => [a] -> [a]
