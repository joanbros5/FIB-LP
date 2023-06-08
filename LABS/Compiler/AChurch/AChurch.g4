// SUPER ULTRA HIPER GRAMATICA CHIQUITA DE LAMBDA CALCUL
grammar AChurch;

root : terme
     ;
     
terme :  VAR                            # variable
      |  '(' terme ')'                  # termePar
      |  LAMBDA  (VAR)+  '.'  terme     # abstraccio  // λ
      |  terme terme                    # aplicacio   // @
      ;

VAR : [a-z] ;
LAMBDA : 'λ' 
       | '\\'
       ;
