
--Import per fer el sort
import Data.List(sort)

--Estructura de Dades
type Pos = (Int, Int)       -- la casella inferior esquerra és (1,1)


--1. Definiu una funció dins :: Pos -> Bool que, donada una posició d’un cavall,
--retorni si aquesta és dins del tauler.
dins :: Pos -> Bool
dins (x,y) = dinsnum x && dinsnum y

dinsnum :: Int -> Bool
dinsnum x = x >= 1 && x <= 8

--2. Definiu una funció moviments :: Pos -> [Pos] que, donada una
--posició d’un cavall dins del tauler, retorni la llista de posicions
--dins del tauler on es pot trobar després d’un salt.
moviments :: Pos -> [Pos]
moviments (x,y) = filter dins [(x+px,y+py) | (px,py) <- [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]]

--3.Definiu una funció potAnar3 :: Pos -> Pos -> Bool que, donada una posició
--inicial p dins del tauler i una posició final q, digui si un cavall pot anar
--de p a q en (exactament) tres salts.

potAnar3 :: Pos -> Pos -> Bool
potAnar3 p1 p2 = any (== p2) (concat $ map moviments $ concat $ map moviments $ moviments p1)


--4. Definiu ara una funció potAnar3’ :: Pos -> Pos -> Bool que faci el mateix
--que potAnar3 però trient partit del fet que les llistes són instància de Monad.

potAnar3' :: Pos -> Pos -> Bool
potAnar3' p1 p2 = p2 `elem` destins
    where destins = (moviments p1 >>= moviments >>= moviments)




