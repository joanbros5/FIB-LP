myFoldl :: (a -> b -> a) -> a -> [b] -> a

myFoldl _ x [] = x
myFoldl f x (y:ys) = myFoldl f (f x y) ys

-------------------------------

myFoldr :: (a -> b -> b) -> b -> [a] -> b

myFoldr _ x [] = x
myFoldr f x (y:ys) = f y (myFoldr f x ys)

-------------------------------

myIterate :: (a -> a) -> a -> [a]

myIterate f a = a : myIterate f (f a)

-------------------------------

myUntil :: (a -> Bool) -> (a -> a) -> a -> a

myUntil f g a
    | f a = a
    | otherwise = myUntil f g (g a)

-------------------------------

myMap :: (a -> b) -> [a] -> [b]

myMap f [] = []
myMap f (x:xs) = f x : (myMap f xs)

-------------------------------

myFilter :: (a -> Bool) -> [a] -> [a]

myFilter f [] = []
myFilter f (x:xs)
    | f x = x:myFilter f xs
    | otherwise = myFilter f xs

-------------------------------

myAll :: (a -> Bool) -> [a] -> Bool

myAll f x = and $ map f x

-------------------------------

myAny :: (a -> Bool) -> [a] -> Bool

myAny f x = or $ map f x

-------------------------------

myZip :: [a] -> [b] -> [(a, b)]

myZip _ [] = []
myZip [] _ = []
myZip (x:xs) (y:ys) = (x,y): myZip xs ys

-------------------------------

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]

myZipWith f x y = [f a b | (a,b) <- myZip x y ]

