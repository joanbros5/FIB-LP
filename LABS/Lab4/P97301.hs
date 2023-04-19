fizzBuzz :: [Either Int String]

fizzBuzz = fizzBuzz2 0


--Funció Auxiliar
fizzBuzz2 :: Int -> [Either Int String]

fizzBuzz2 x
    | x `mod` 15 == 0 = (Right "FizzBuzz") : fizzBuzz2 (x+1)
    | x `mod` 3 == 0 = (Right "Fizz") : fizzBuzz2 (x+1)
    | x `mod` 5 == 0 = (Right "Buzz") : fizzBuzz2 (x+1)
    | otherwise = (Left x) : fizzBuzz2 (x+1)
