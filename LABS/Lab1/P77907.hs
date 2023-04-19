absValue :: Int -> Int

absValue n
    | n>= 0 = n
    | otherwise = -n

---------------------------------------------------------------

power :: Int -> Int -> Int

power _ 0 = 1
power x y
    | even y = n * n
    | otherwise = n * n * x
    where
        n = power x n_mig
        n_mig = div y 2

---------------------------------------------------------------

primer :: Int -> Int -> Bool

primer 0 _ = False
primer 1 _ = False
primer n i
    | mod n i == 0 = False
    | i*i > n = True
    | otherwise = primer n (i+1)

isPrime :: Int -> Bool

isPrime 0 = False
isPrime 1 = False
isPrime 2 = True
isPrime n = primer n 2

---------------------------------------------------------------

slowFib :: Int -> Int

slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)

---------------------------------------------------------------


-- Teorema:

-- Donats F(k) i F(k+1), podem calcular:
-- F(2k)   = F(k)[2F(k+1)-F(k)]
-- F(2k+1) = F(k+1)^2+F(k)^2

-- Font: https://www.nayuki.io/page/fast-fibonacci-algorithms

quickFib :: Int -> Int

quickFib n
    | n>= 0 = fst (fibonacci n)

fibonacci :: Int -> (Int, Int)

fibonacci 0 = (0,1)
fibonacci n =
    let (a,b) = fibonacci (div n 2)
        c = a * (b*2 - a)
        d = a*a + b*b
    in  if mod n 2 == 0 then (c,d)
        else (d, c + d)
