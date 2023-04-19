myLength :: [Int] -> Int

myLength [] = 0
myLength (_:xs) = myLength xs + 1

-------------------------------

myMaximum :: [Int] -> Int

myMaximum [x] = x
myMaximum llista = max cap resta
    where
        cap = head llista
        resta = myMaximum (tail llista)

-------------------------------

average :: [Int] -> Float

average [] = 0
average llista = suma / tamany
    where
        suma = fromIntegral (sum llista)
        tamany = fromIntegral (myLength llista)

-------------------------------

buildPalindrome :: [Int] -> [Int]

buildPalindrome llista = reverse llista ++ llista

-------------------------------

--S'ha d'usar la funció "elem": elem x xs indica si x és a la llista xs.
remove :: [Int] -> [Int] -> [Int]

remove [] _ = []
remove (x:xs) ys
    | elem x ys = remove xs ys
    | otherwise = x : remove xs ys

-------------------------------

flatten :: [[Int]] -> [Int]

flatten [] = []
flatten (x:xs) = x ++ flatten xs

-------------------------------

oddsNevens :: [Int] -> ([Int],[Int])

oddsNevens xs = (odds xs, evens xs)

odds :: [Int] -> [Int]

odds [] = []
odds (x:xs)
    | odd x = x : odds xs
    | otherwise = odds xs

evens :: [Int] -> [Int]

evens [] = []
evens (x:xs)
    | even x = x : evens xs
    | otherwise = evens xs

-------------------------------

primeDivisors :: Int -> [Int]

primeDivisors n = filter isPrime (divisors n)
    where
        isPrime k = null [x | x<-[2..k-1], k `mod` x == 0]
        divisors n = [x | x<-[2..n], n `mod` x == 0]
