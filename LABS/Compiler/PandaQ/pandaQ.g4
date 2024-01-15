//SUPER ULTRA HIPER GRAMATICA DE SQL
grammar pandaQ;

root : (query)+
	 ;

query : selectQ
	  ;

selectQ : select camps from taula (orderby)? (where)? ';'		#selectExpr
	    ;

orderby : ('order by' | 'ORDER BY') orderparam (',' orderparam)*	#orderByExpr
		;

orderparam : ID ('asc' | 'desc')? 	#orderParamExpr
		   ;
		   
where : ('WHERE' | 'where') condicions		#whereExpr
	  ;

condicions : '(' condicions ')'				#condicioParentesis
		   | condicio 'and' condicions		#condicioAnd
		   | condicio 'or' condicions		#condicioOr
		   | condicio						#condicioSingle
		   ;

condicio : ('not')? camp operadorBool operacio		#condicioExpr
		 ;
		 
operadorBool : '<' | '=' ;

camps : '*' 				#allCamps
	  | camp (',' camp)*	#listCamps
	  ;
	  
camp : ID '+' operacio 'as' ID		#campCalculatS
	 | ID '-' operacio 'as' ID		#campCalculatR
	 | ID '*' operacio 'as' ID		#campCalculatM
	 | ID '/' operacio 'as' ID		#campCalculatD
	 | ID '^' operacio 'as' ID		#campCalculatP
	 | ID							#campNoCalculat
	 ;

	 
operacio : '(' operacio ')'			  			# parentesis
	 | <assoc=right> operacio '^' operacio   	# pot
     | operacio '/' operacio    				# div
     | operacio '*' operacio    				# mul
     | operacio '-' operacio    				# resta
     | operacio '+' operacio    				# suma
     | NUM              						# numero
     ;
	  
//Per ser fidel al SQL original permeto majúscules 
select : 'select' | 'SELECT' ;
from : 'from' | 'FROM' ;

taula : ID ;

ID : [a-zA-Z_\-0-9]+ ;
NUM : INT | FLOAT ;
INT : [0-9]+ ;
FLOAT : INT '.' INT ;
WS : [ \t\r\n]+ -> skip;	//Per ignorar espais en blanc
