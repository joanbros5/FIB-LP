from __future__ import annotations
from dataclasses import dataclass
from antlr4 import *
from AChurchLexer import AChurchLexer
from AChurchParser import AChurchParser
from AChurchVisitor import AChurchVisitor

#############################
#        TREE CLASS         #
#############################

class Buit:
    pass

@dataclass
class Node:
    val: string
    esq: Arbre
    dre: Arbre

Arbre = Node | Buit

def mida(a: Arbre) -> int:
    match a:
        case Buit():
            return 0
        case Node(x, e, d):
            return 1 + mida(e) + mida(d)


#############################
#          VISITOR          #
#############################


class TreeVisitor(AChurchVisitor):

    def __init__(self):
        self.tree = Node(0, Buit, Buit)
        
    def visitRoot(self,ctx):
        children = list(ctx.getChildren())
        for c in children:
            self.visit(c)
            
    def visitAplicacio(self,ctx):
        [term1, term2] = list(ctx.getChildren())
        return Node('@', self.visit(term1), self.visit(term2))
            
    def visitVariable(self,ctx):
        [variable] = list(ctx.getChildren())
        return Node(variable.getText(), Buit, Buit)
            


#############################
#        EVALUATOR          #
#############################


class EvalVisitor(AChurchVisitor):
    
    def __init__(self):
        self.variables = {
        }
        self.funcions = {
        }


#############################
#          SCRIPT           #
#############################


def evaluate():
    print()
    print('____EVALUATION____')
    evaluator = EvalVisitor()
    evaluator.visit(tree)
    
def printTree():
    print()
    print('____TREE____')
    visitor = TreeVisitor()
    visitor.visit(tree)
    
def printExpr():
    print()
    print('____EXPRESSION____')
    print(tree.toStringTree(recog=parser))
    print()


#ENTRADA DESDE INPUT.TXT O MANUAL (entrada d'input.txt no detecta el caràcter 'λ', la manual si)
#input_stream = InputStream(input('? '))
input_stream = FileStream('input.txt')


lexer = AChurchLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = AChurchParser(token_stream)
tree = parser.root()

#COMENTAR PER FER LA SORTIDA SEGONS COM VULGUIS
#evaluate()
printTree()
printExpr()
