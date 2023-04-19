main = do
    line <- getLine
    if line == "" then return ()
    else if last line == 'a' || last line == 'A' then do
        putStrLn "Hola maca!"
    else do
        putStrLn "Hola maco!"
