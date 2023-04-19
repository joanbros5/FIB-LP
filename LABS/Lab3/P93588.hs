
-- Aplica una funcio f a tots els elements d'una llista
-- Retorna una llista amb tots els resultats
myMap :: (a -> b) -> [a] -> [b]

myMap f llista = [f x | x <- llista]

-------------------------------

-- Retorna una llista amb els elements que compleixin la condicio f de una llista donada
myFilter :: (a -> Bool) -> [a] -> [a]

myFilter f llista = [x | x <- llista, f x]

-------------------------------

-- Retorna una llista que opera els elements de dues llistes un a un amb la funcio f
myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]

myZipWith f xs ys = [f a b | (a,b) <- zip xs ys]

-------------------------------

-- Donades dues llistes d’enters, genera la llista que aparella els elements si l’element
-- de la segona llista divideix al de la primera.
thingify :: [Int] -> [Int] -> [(Int, Int)]

thingify xs ys = [(x,y) | x <- xs, y <- ys, x `mod` y == 0]

-------------------------------

-- Donat un natural no nul, genera la llista ordenada amb els seus factors (no necessàriament primers)
factors :: Int -> [Int]

factors n = [x | x <- [1..n] , n `mod` x == 0]
