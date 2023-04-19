data Expr = Val Int | Add Expr Expr | Sub Expr Expr | Mul Expr Expr | Div Expr Expr

-- Donada una expressió, retorna la seva avaluació. Mai hi haurà divisions per zero.

eval1 :: Expr -> Int

eval1 (Val x) = x
eval1 (Add e1 e2) = eval1 e1 + eval1 e2
eval1 (Sub e1 e2) = eval1 e1 - eval1 e2
eval1 (Mul e1 e2) = eval1 e1 * eval1 e2
eval1 (Div e1 e2) = div (eval1 e1) (eval1 e2)

-- Donada una expressió, retorna la seva avaluació com un valor Just.
-- En el cas que es produeixi una divisió per zero, el resultat ha de ser Nothing.

eval2 :: Expr -> Maybe Int

eval2 (Val x) = Just x
eval2 (Add e1 e2) = do
    x <- eval2 e1   --Desempaqueta e1 a x
    y <- eval2 e2   --Desempaqueta e2 a y
    return (x + y)  --Empaqueta x + y == Just (x + y)

    -- Format Monada:
    -- eval2 e1 >>= \x ->
        -- eval2 e2 >>= \y ->
            -- return (x + y)

eval2 (Sub e1 e2) = do
    x <- eval2 e1
    y <- eval2 e2
    Just (x - y)

eval2 (Mul e1 e2) = do
    x <- eval2 e1
    y <- eval2 e2
    Just (x * y)

eval2 (Div e1 e2) = do
    x <- eval2 e1
    y <- eval2 e2
    if y == 0 then Nothing else Just (div x y)


-- Donada una expressió, retorna la seva avaluació com un valor Right.
-- En el cas que es produeixi una divisió per zero, el resultat ha de ser Left "div0" per indicar l’error en qüestió.

eval3 :: Expr -> Either String Int

eval3 (Val x) = Right x
eval3 (Add e1 e2) = do
    x <- eval3 e1   --Desempaqueta e1 a x
    y <- eval3 e2   --Desempaqueta e2  y
    return (x + y)  --Empaqueta x + y == Right (x + y) o bé Left ("div0")

eval3 (Sub e1 e2) = do
    x <- eval3 e1
    y <- eval3 e2
    return (x - y)

eval3 (Mul e1 e2) = do
    x <- eval3 e1
    y <- eval3 e2
    return (x * y)

eval3 (Div e1 e2) = do
    x <- eval3 e1
    y <- eval3 e2
    if y == 0 then Left "div0" else return (div x y)





