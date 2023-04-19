-- Funcio que diu els moviments
moviments :: Integer -> String -> String -> String -> [String]

moviments 0 _ _ _ = []
moviments 1 ti tf _ = [ti ++ " -> " ++ tf]
moviments n ti tf taux = moviments (n-1) ti taux tf ++ moviments 1 ti tf taux ++ moviments (n-1) taux tf ti


--Funcio per interpretar la entrada
torresHanoi :: String -> [String]

torresHanoi line = moviments (read(ndiscs) :: Integer) ti tf taux

    where [ndiscs,ti,tf,taux] = words line

--MAIN
main = do
    line <- getLine

    mapM_ putStrLn (torresHanoi line)

    return()
