-- 1. Escriviu una funció multEq :: Int -> Int -> [Int] que, donats dos nombres positius x i y
-- diferents de zero, genera la llista infinita ordenada creixentment que conté els nombres
-- formats per la multiplicació de la mateixa quantitat de x que de y.

multEq :: Int -> Int -> [Int]

multEq x y = [1] ++ [x^num*y^num | num <- [1..]]


-- 2. Escriviu una funció selectFirst :: [Int] -> [Int] -> [Int] -> [Int] que, donades tres
-- llistes l1, l2 i l3 retona els elements de l1 que apareixen a l2 en una posició menor
-- estrictament que a l3. Si un element apareix a l2 i no a l3 es considera que apareix en
-- una posició anterior.

selectFirst :: [Int] -> [Int] -> [Int] -> [Int]

selectFirst [] _ _ = []
selectFirst l1 l2 l3 = filter (esta l2 l1) l1

esta :: [Int] -> [Int] -> Bool
esta [] _ = False
esta (x:xs) l1 = elem x l1 && esta xs l1
