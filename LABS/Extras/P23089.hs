import Data.List (unfoldr)

-- 1. Definiu recursivament una funció
-- myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a] que funcioni com unfoldr.
-- Si no us en sortiu, podeu fer la resta dels apartats fent
-- myUnfoldr = unfoldr i incloent un import Data.List (unfoldr) al principi del programa.

myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]

--myUnfoldr = unfoldr

myUnfoldr f x = case f x of
    Nothing -> []
    Just (a, b) -> a : myUnfoldr f b


-- 2. Definiu, utilitzant myUnfoldr, una funció
-- myReplicate :: a -> Int -> [a] de manera que myReplicate x n
-- retorni una llista amb n cops el valor x.

myReplicate :: a -> Int -> [a]

myReplicate x n = myUnfoldr (\n -> if n <= 0 then Nothing else Just (x, n-1)) n

-- 3. Definiu, utilitzant myUnfoldr, una funció
-- myIterate :: (a -> a) -> a -> [a] que funcioni com iterate.

myIterate :: (a -> a) -> a -> [a]

myIterate f n = myUnfoldr (\n -> Just (n,f n)) n

-- 4. Definiu, utilitzant myUnfoldr, una funció
-- myMap :: (a -> b) -> [a] -> [b] que funcioni com map

myMap :: (a -> b) -> [a] -> [b]

myMap f x = myUnfoldr (\x -> if null x then Nothing else Just (f (head x), tail x)) x

-- 5. Considereu la definició següent del tipus Bst per arbres binaris
-- de cerca, juntament amb una funció add que hi afegeix valors:

data Bst a = Empty | Node a (Bst a) (Bst a) --deriving Show

add :: Ord a => a -> (Bst a) -> (Bst a)

add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y          = Node y (add x l) r
    | x > y          = Node y l (add x r)
    | otherwise      = Node y l r

-- Feu que els arbres binaris de cerca siguin instància de Show, mostrant-se segons els exemples.

instance Show a => Show (Bst a) where
    show Empty = "."
    show (Node x fe fd) = "(" ++ show x ++ " " ++ show fe ++ " " ++ show fd ++ ")"

-- 6. Definiu una funció adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
-- de manera que myUnfoldr adder (t, xs) retorni una llista que mostri, pas a pas,
-- la construcció d’un arbre binari de cerca inserint seqüencialment els valors de xs en t. Vegeu l’exemple.

adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
adder (t, []) = Nothing
adder (t, (x:xs)) = Just (new, (new, xs))
    where
        new = add x t
