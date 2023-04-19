
-- Estructura de l'arbre
data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)


-- BD pel joc de proves
t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2
t8 = Node 8 t1 t3


-- 1.Feu una funció size :: Tree a -> Int que, donat un arbre, retorni la seva talla,
-- és a dir, el nombre de nodes que conté.

size :: Tree a -> Int

size Empty = 0
size (Node _ fe fd) = 1 + size fe + size fd

-- 2.Feu una funció height :: Tree a -> Int que, donat un arbre, retorni la seva alçada,
-- assumint que els arbres buits tenen alçada zero.

height :: Tree a -> Int

height Empty = 0
height (Node _ fe fd) = 1 + max (height fe) (height fd)

-- 3.Feu una funció equal :: Eq a => Tree a -> Tree a -> Bool que, donat dos arbres,
-- indiqui si són el mateix.

equal :: Eq a => Tree a -> Tree a -> Bool

equal Empty Empty = True
equal Empty y = False
equal x Empty = False
equal (Node x fex fdx) (Node y fey fdy) = x == y && (equal fex fey) && (equal fdx fdy)

-- 4.Feu una funció isomorphic :: Eq a => Tree a -> Tree a -> Bool que, donat un arbres,
-- indiqui si són el isomorfs, és a dir, si es pot obtenir l’un de l’altre tot girant
-- algun dels seus fills.

isomorphic :: Eq a => Tree a -> Tree a -> Bool

isomorphic Empty Empty = True
isomorphic Empty y = False
isomorphic x Empty = False
isomorphic (Node x fex fdx) (Node y fey fdy) = x == y && ((equal fex fey) && (equal fdx fdy) || (equal fdx fey) && (equal fex fdy))

-- 5.Feu una funció preOrder :: Tree a -> [a] que, donat un arbre, retorni el seu
-- recorregut en pre-ordre.

preOrder :: Tree a -> [a]

preOrder Empty = []
preOrder (Node x fe fd) = [x] ++ preOrder fe ++ preOrder fd

-- 6.Feu una funció postOrder :: Tree a -> [a] que, donat un arbre, retorni el seu
-- recorregut en post-ordre.

postOrder :: Tree a -> [a]

postOrder Empty = []
postOrder (Node x fe fd) = postOrder fe ++ postOrder fd ++ [x]

-- 7.Feu una funció inOrder :: Tree a -> [a] que, donat un arbre, retorni el seu
-- recorregut en in-ordre.

inOrder :: Tree a -> [a]

inOrder Empty = []
inOrder (Node x fe fd) = inOrder fe ++ [x] ++ inOrder fd

-- 8.Feu una funció breadthFirst :: Tree a -> [a] que, donat un arbre, retorni el seu
-- recorregut per nivells.

breadthFirst :: Tree a -> [a]

breadthFirst t = breadth [t]


breadth :: [Tree a] -> [a]

breadth [] = []
breadth (Empty:trees) = breadth trees
breadth ((Node x fe fd):trees) = x : (breadth (trees ++ [fe, fd]))

-- 9.Feu una funció build :: Eq a => [a] -> [a] -> Tree a que, donat el recorregut en
-- pre-ordre d’un arbre i el recorregut en in-ordre del mateix arbre, retorni l’arbre
-- original. Assumiu que l’arbre no té elements repetits.

build :: Eq a => [a] -> [a] -> Tree a

build [] [] = Empty
build (x:xs) y = Node x (build fille llistae) (build filld llistad)
    where
        fille = take (length llistae) xs
        filld = drop (length llistae) xs
        llistae = takeWhile (/= x) y
        llistad = tail (dropWhile (/= x) y)

-- 10.Feu una funció overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a que, donats
-- dos arbres, retorni la seva superposició utilitzant una funció. Superposar dos arbres
-- amb una funció consisteix en posar els dos arbres l’un damunt de l’altre i combinar els
-- nodes doble resultants amb la funció donada o deixant els nodes simples tal qual.

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a

overlap _ x Empty = x
overlap _ Empty y = y
overlap f (Node x fex fdx) (Node y fey fdy) = Node (f x y) (overlap f fex fey) (overlap f fdx fdy)

