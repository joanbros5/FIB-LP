from antlr4 import *
from pandaQLexer import pandaQLexer
from pandaQParser import pandaQParser
from pandaQVisitor import pandaQVisitor

# Exclusiu per aquesta pràctica #
import streamlit as st
import pandas as pd


#############################
#          VISITOR          #
#############################

## No l'utilitzo en aquesta pràctica 

#############################
#        EVALUATOR          #
#############################

class EvalVisitor(pandaQVisitor):
    
    def __init__(self):
        self.datapath = "./data/"
        self.file = ""
        self.campsCalculats = {
        }
        self.orderbyParams = {
        }
        
    def visitRoot(self, ctx):
        children = list(ctx.getChildren())
        for c in children:
            self.visit(c)
            
    def visitQuery(self, ctx):
        children = list(ctx.getChildren())
        for c in children:
            self.visit(c)
        
    def visitSelectExpr(self, ctx):
        children = list(ctx.getChildren())
        
        selectword = None
        camps = None
        fromword = None
        taula = None
        orderby = None
        where = None
        puntcoma = None
        
        if len(children) >= 5:
            selectword, camps, fromword, taula, *resta = children
            
            for elem in resta:
                if 'order by' in elem.getText().lower():
                    orderby = elem
                if 'where' in elem.getText().lower():
                    where = elem
                if elem.getText() == ';':
                    puntcoma = elem
        
        #DEBUG
        #print("Camps: " + camps.getText())
        
        self.file = pd.read_csv(self.datapath + taula.getText() + ".csv")
        
        # Seleccio de camps
        if camps.getText() != '*':
            self.file = self.file[self.visit(camps)]
            if not self.campsCalculats == {}:
                for cc in list(self.campsCalculats.keys()):
                    self.file[cc] = self.campsCalculats[cc]
        
        # Condicions i ordenacio
        
        self.file = self.file.query(self.visit(where))
        
        orderby_list = []
        
        if orderby != None:
            self.visit(orderby)
            
            orderby_list = [(col, True) if order.lower() == 'asc' else (col, False) for col, order in self.orderbyParams.items()]
        
        st.dataframe(self.file.sort_values(by=[col[0] for col in orderby_list], ascending= [order[1] for order in orderby_list]))
            
    def visitOrderByExpr(self,ctx):
        [orderword, *resta] = list(ctx.getChildren())
        
        for p in resta:
            self.visit(p)
    
    def visitOrderParamExpr(self,ctx):
        children = list(ctx.getChildren())
        
        if len(children) > 1:
            self.orderbyParams[children[0].getText()] = children[1].getText()
        else:
            self.orderbyParams[children[0].getText()] = 'asc'
            
        # DEBUG
        #print(children[0].getText() + ' es ' + self.orderbyParams[children[0].getText()])
    
    ##############
    ##CONDICIONS
    ##############
    def visitWhereExpr(self,ctx):
        [where, conds] = list(ctx.getChildren())
        
        # Retorna un string amb totes les condicions pel filtrat
        return self.visit(conds)
    
    def visitCondicioParentesis(self,ctx):
        [par1, cond, par2] = list(ctx.getChildren())
        
        return '(' + self.visit(cond) + ')'
    
    def visitCondicioAnd(self,ctx):
        [cond1, andw, conds] = list(ctx.getChildren())
        
        return self.visit(cond1) + ' and ' + self.visit(conds)
    
    def visitCondicioOr(self,ctx):
        [cond1, orw, conds] = list(ctx.getChildren())
        
        return self.visit(cond1) + ' or ' + self.visit(conds)
    
    def visitCondicioSingle(self, ctx):
        [cond] = list(ctx.getChildren())
        return self.visit(cond)
        
    def visitCondicioExpr(self,ctx):
        children = list(ctx.getChildren())
        
        if len(children) > 3:
            [notword, camp, opbool, operacio] = children
            opB = '==' if opbool.getText() == '=' else opbool.getText()
            
            return 'not ' + camp.getText() + opB + str(self.visit(operacio))
        
        else:
            [camp, opbool, operacio] = children
            opB = '==' if opbool.getText() == '=' else opbool.getText()
            
            return camp.getText() + opB + str(self.visit(operacio))
        
        
    #############
    ##CAMPS
    #############
    def visitListCamps(self, ctx):
        camps = list(ctx.getChildren())
        
        campList = []
        
        for c in camps:
            if c.getText() != ',':
                if self.visit(c) != '-1_c_calculat':
                    campList.append(self.visit(c))
        return campList
    
    def visitCampNoCalculat(self, ctx):
        [ID] = list(ctx.getChildren())
        return ID.getText()
            
    #####################
    ##### CAMPS CALCULATS
    #####################
    def visitCampCalculatS(self, ctx):
        [campOri, suma, ops, asWord, campNou ] = list(ctx.getChildren())
        
        self.campsCalculats[campNou.getText()] = self.file[campOri.getText()].apply(lambda x: x + self.visit(ops))
        return "-1_c_calculat"
    
    def visitCampCalculatR(self, ctx):
        [campOri, resta, ops, asWord, campNou ] = list(ctx.getChildren())
        
        self.campsCalculats[campNou.getText()] = self.file[campOri.getText()].apply(lambda x: x - self.visit(ops))
        return "-1_c_calculat"
    
    def visitCampCalculatM(self, ctx):
        [campOri, mul, ops, asWord, campNou ] = list(ctx.getChildren())
        
        self.campsCalculats[campNou.getText()] = self.file[campOri.getText()].apply(lambda x: x * self.visit(ops))
        return "-1_c_calculat"
    
    def visitCampCalculatD(self, ctx):
        [campOri, div, ops, asWord, campNou ] = list(ctx.getChildren())
        
        self.campsCalculats[campNou.getText()] = self.file[campOri.getText()].apply(lambda x: x / self.visit(ops))
        return "-1_c_calculat"
    
    def visitCampCalculatP(self, ctx):
        [campOri, pot, ops, asWord, campNou ] = list(ctx.getChildren())
        
        self.campsCalculats[campNou.getText()] = self.file[campOri.getText()].apply(lambda x: x ** self.visit(ops))
        return "-1_c_calculat"
        
    def visitParentesis(self, ctx):
        [par1, op, par2] = list(ctx.getChildren())
        return self.visit(op)
    
    def visitSuma(self, ctx):
        [op1, operador, op2] = list(ctx.getChildren())
        return self.visit(op1) + self.visit(op2)
    
    def visitResta(self, ctx):
        [op1, operador, op2] = list(ctx.getChildren())
        return self.visit(op1) - self.visit(op2)
    
    def visitMul(self, ctx):
        [op1, operador, op2] = list(ctx.getChildren())
        return self.visit(op1) * self.visit(op2)
    
    def visitDiv(self, ctx):
        [op1, operador, op2] = list(ctx.getChildren())
        return self.visit(op1) / self.visit(op2)
    
    def visitPot(self, ctx):
        [op1, operador, op2] = list(ctx.getChildren())
        return self.visit(op1) ** self.visit(op2)
    
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return float(numero.getText())
            
    def visitID(self, ctx):
        [ID] = list(ctx.getChildren())
        return ID.getText()
    
            

#############################
#          SCRIPT           #
#############################

def parse_sql_query(query):
    
    lexer = pandaQLexer(InputStream(query))
    stream = CommonTokenStream(lexer)
    parser = pandaQParser(stream)

    tree = parser.root()
    
    #DEBUG
    #print("Query: " + query)
    
    if parser.getNumberOfSyntaxErrors() > 0:
        return "Introdueix una consulta vàlida. Es poden veure els errors gramaticals en la terminal."
    else:
        evaluator = EvalVisitor()
        evaluator.visit(tree)
        
        return "Consulta SQL analitzada correctament."

st.title("Ultra compilador de SQL")

sql_query = st.text_area("Query:", "")

if st.button("Submit"):
    
    #Per separar els outputs de querys en la terminal
    print("-----------------------------")
    
    if sql_query:
        # Analitzar la consulta
        result = parse_sql_query(sql_query)
        if 'correctament' in result:
            st.success(result)
            
            # Marcar la correctesa per terminal
            print("Tot correcte")
        else:
            st.error(result)
    else:
        st.warning("No introdueixis una consulta buida sisplau.")
