// Gramàtica per expressions senzilles
grammar exprs;

root : (function)* main
     ;
     
function : 'function' cap (instr)* 'end'
         ;
         
cap : VAR '(' (parametres)? ')'
    ;
    
parametres : VAR (',' VAR)*
           ;
     
main : 'main' (instr)* 'end'  # mainExp
     ;
     
instr : printat     # write
      | assig       # assignacio
      | condnal		# condicional
      | bucle       # while
      | return      # returnInstr
      ;
      
return : 'return' expr
       ;
      
printat : 'write' expr  # writeExp
        ;
      
assig : VAR ':=' expr   # assigExp
      ;
      
condnal : 'if' condicio 'then' (instr)* 'end'	# condnalExp
        ;
     
bucle : 'while' condicio 'do' (instr)* 'end'    #bucleExp
      ;
     
condicio : expr operador expr	# condicioExp
         ;
     
expr : <assoc=right> expr '^' expr    # pot
     | expr '/' expr    # div
     | expr '*' expr    # mul
     | expr '-' expr    # resta
     | expr '+' expr    # suma
     | VAR              # variable
     | NUM              # numero
     | cap              # capFuncio
     ;
     
operador : '=='   # eq
         | '<='   # se
         | '>='   # ge
         | '<'    # st
         | '>'    # gt
         | '!='   # neq
         ;

VAR : [a-z]+ ;
NUM : [0-9]+ ;
WS  : [ \t\n\r]+ -> skip ;
