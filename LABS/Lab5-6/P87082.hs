--Funció que determina IMC
veredicte :: Double -> String
veredicte value
    | value < 18 = "magror"
    | value < 25 = "corpulencia normal"
    | value < 30 = "sobrepes"
    | value < 40 = "obesitat"
    | otherwise = "obesitat morbida"

--Transformat de tipus de dades
imc :: String -> String -> String
imc weight height = veredicte (w / (h*h))
    where
        --read és una funció que transforma un String al tipus que se li especifica
        w = read(weight) :: Double
        h = read(height) :: Double

--Prepara el format de sortida, separa les dades i calcula
calculate :: String -> String
calculate line = name ++ ": " ++ imc weight height
    where
        --words és una funció String -> [String] que separa les paraules per espais
        [name,weight,height] = words line

--MAIN
main = do
    line <- getLine

    if line/="*" then do
        putStrLn $ calculate line
        main
    else
        return()
