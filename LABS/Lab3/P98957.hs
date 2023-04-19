ones :: [Integer]

ones = 1 : ones

-------------------------------

nats :: [Integer]

nats = 0 : map (+1) nats

-------------------------------

-- concat concatena listas de listas en una lista, para concatenar los [x,-x]
ints :: [Integer]

ints = 0 : concat [[x,-x] | x <- tail nats]

-------------------------------

triangulars :: [Integer]

triangulars = scanl (+) 0 (tail nats)

-------------------------------

factorials :: [Integer]

factorials = scanl (*) 1 (tail nats)

-------------------------------

fibs :: [Integer]

fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

-------------------------------

primes :: [Integer]

primes = garbell (drop 2 nats)
    where
        garbell (p:xs) = p : garbell [x | x <- xs, x `mod` p /= 0]

-------------------------------

hammings :: [Integer]

hammings = 1 : merge (map (*2) hammings) (merge (map (*3) hammings) (map (*5) hammings))

-- Funció auxiliar
merge :: [Integer] -> [Integer] -> [Integer]

merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x < y = x : merge xs (y:ys)
    | y < x = y : merge (x:xs) ys
    | otherwise = x : merge xs ys

-------------------------------

lookNsay :: [Integer]

lookNsay = iterate (read.say.show) 1

--Auxs
look :: [Char] -> Integer

look [] = 0
look [_] = 1
look (c1:c2:s)
    | c1 == c2 = 1 + look (c2:s)
    | otherwise = 1

say :: [Char] -> [Char]

say [] = []
say s = show (look s) ++ head s : say (drop (fromIntegral (look s)) s)

-------------------------------

tartaglia :: [[Integer]]

--              \x = Lambda x, (función sin nombre) ("Dada una x hazme un zipwith...")
tartaglia = iterate (\x -> zipWith (+) (0 : x) (x ++ [0])) [1]
