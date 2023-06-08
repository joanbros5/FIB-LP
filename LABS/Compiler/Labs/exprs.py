from antlr4 import *
from exprsLexer import exprsLexer
from exprsParser import exprsParser
from exprsVisitor import exprsVisitor


#############################
#          VISITOR          #
#############################


class TreeVisitor(exprsVisitor):

    def __init__(self):
        self.nivell = 0
        
    def visitRoot(self,ctx):
        children = list(ctx.getChildren())
        for c in children:
            self.visit(c)
            
    def visitFunction(self, ctx):
        children = list(ctx.getChildren())
        for i in range(1, len(children) - 1):
            if i != 1:
                print('   ' * self.nivell + 'instruccio')
                self.nivell += 1
            self.visit(children[i])
            if self.nivell > 0:
                self.nivell -= 1
            print('   ' * self.nivell + '----------')
        print('FUNCTION END')
        print()
            
    def visitReturn(self, ctx):
        [ret, expressio] = list(ctx.getChildren())
        print('   ' * self.nivell + 'return')
        self.nivell += 1
        self.visit(expressio)
        self.nivell -= 1
        
    def visitCap(self, ctx):
        cap = list(ctx.getChildren())
        print('   ' * self.nivell + 'FUNCTION ' + cap[0].getText())
        self.nivell += 1
        for i in range(2, len(cap) - 1):
            self.visit(cap[i])
        self.nivell -= 1
            
    def visitParametres(self, ctx):
        parametres = list(ctx.getChildren())
        print('parameters: ')
        for p in parametres:
            print(str(p), end='')
        print()
        
    def visitMainExp(self, ctx):
        children = list(ctx.getChildren())
        print('   ' * self.nivell + 'MAIN')
        print('   ' * self.nivell + '----------')
        for i in range(1, len(children)-1):
            print('   ' * self.nivell + 'instruccio')
            self.nivell += 1
            self.visit(children[i])
            self.nivell -= 1
            print('   ' * self.nivell + '----------')
        print('MAIN END')
        
    def visitWrite(self, ctx):
        [writeExp] = list(ctx.getChildren())
        print('   ' * self.nivell + 'write')
        self.nivell += 1
        self.visit(writeExp)
        self.nivell -= 1
        
    def visitAssignacio(self, ctx):
        [assigExp] = list(ctx.getChildren())
        print('   ' * self.nivell + 'assig')
        self.nivell += 1
        self.visit(assigExp)
        self.nivell -= 1
        
    def visitAssigExp(self, ctx):
        [variable, equals, expressio] = list(ctx.getChildren())
        print('   ' * self.nivell +variable.getText() + ':=')
        self.nivell += 1
        self.visit(expressio)
        self.nivell -=1
        
    def visitCondicional(self, ctx):
        [assigExp] = list(ctx.getChildren())
        print('   ' * self.nivell + 'cond')
        self.nivell += 1
        self.visit(assigExp)
        self.nivell -= 1
        
    def visitCondnalExp(self, ctx):
        children = list(ctx.getChildren())
        print('   ' * self.nivell + 'if')
        self.nivell += 1
        self.visit(children[1])
        self.nivell -= 1
        print('   ' * self.nivell + 'then')
        self.nivell += 1
        
        print('   ' * self.nivell + '----------')
        
        for i in range(3, len(children)-1):
            self.visit(children[i])
            print('   ' * self.nivell + '----------')
        self.nivell -=1
        print('   ' * self.nivell + 'end')
        
    def visitWhile(self, ctx):
        [assigExp] = list(ctx.getChildren())
        print('   ' * self.nivell + 'bucle')
        self.nivell += 1
        self.visit(assigExp)
        self.nivell -= 1
        
    def visitBucleExp(self, ctx):
        children = list(ctx.getChildren())
        print('   ' * self.nivell + 'while')
        self.nivell += 1
        self.visit(children[1])
        self.nivell -= 1
        print('   ' * self.nivell + 'do')
        self.nivell += 1
        
        print('   ' * self.nivell + '----------')
        
        for i in range(3, len(children)-1):
            self.visit(children[i])
            print('   ' * self.nivell + '----------')
        self.nivell -=1
        print('   ' * self.nivell + 'end')
        
    def visitCondicioExp(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + operador.getText())
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitSuma(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + '+')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitResta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + '-')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitMul(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + '*')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitDiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + '/')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitPot(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        print('   ' * self.nivell + '^')
        self.nivell += 1
        self.visit(expressio1)
        self.visit(expressio2)
        self.nivell -= 1
        
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        print("   " * self.nivell + numero.getText())
        
    def visitVariable(self, ctx):
        [variable] = list(ctx.getChildren())
        print("   " * self.nivell + variable.getText())
        
        
#############################
#        EVALUATOR          #
#############################


class EvalVisitor(exprsVisitor):
    
    def __init__(self):
        self.variables = {
        }
        self.funcions = {
        }
    
    def visitRoot(self, ctx):
        children = list(ctx.getChildren())
        for c in children:
            self.visit(c)
            
    def visitWriteExp(self, ctx):
        [write, expressio] = list(ctx.getChildren())
        print (self.visit(expressio))
        
    def visitAssigExp(self, ctx):
        [variable, igual, expressio] = list(ctx.getChildren())
        
        #UNCOMMENT TO SEE VARIABLE ASSIGNATIONS IN THE OUTPUT
        #print (variable.getText() + ' <- ' + str(self.visit(expressio)))
        
        self.variables[variable.getText()] = self.visit(expressio)
        
    def visitCondnalExp(self,ctx):
        children = list(ctx.getChildren())
        if self.visit(children[1]):
            for i in range(3, len(children)-1):
                self.visit(children[i])
                
    def visitBucleExp(self,ctx):
        children = list(ctx.getChildren())
        while self.visit(children[1]):
            for i in range(3, len(children)-1):
                self.visit(children[i])
        
    def visitCondicioExp(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        if operador.getText() == '==':
            return self.visit(expressio1) == self.visit(expressio2)
        elif operador.getText() == '<=':
            return self.visit(expressio1) <= self.visit(expressio2)
        elif operador.getText() == '>=':
            return self.visit(expressio1) >= self.visit(expressio2)
        elif operador.getText() == '<':
            return self.visit(expressio1) < self.visit(expressio2)
        elif operador.getText() == '>':
            return self.visit(expressio1) > self.visit(expressio2)
        elif operador.getText() == '!=':
            return self.visit(expressio1) != self.visit(expressio2)
        return False
        
    def visitSuma(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) + self.visit(expressio2)
    
    def visitResta(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) - self.visit(expressio2)
    
    def visitMul(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) * self.visit(expressio2)
    
    def visitDiv(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) / self.visit(expressio2)
    
    def visitPot(self, ctx):
        [expressio1, operador, expressio2] = list(ctx.getChildren())
        return self.visit(expressio1) ** self.visit(expressio2)
    
    def visitNumero(self, ctx):
        [numero] = list(ctx.getChildren())
        return int(numero.getText())
    
    def visitVariable(self, ctx):
        [variable] = list(ctx.getChildren())
        return self.variables[variable.getText()]


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
    

input_stream = FileStream('input.txt')
lexer = exprsLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = exprsParser(token_stream)
tree = parser.root()

#COMMENT THESE INDIVIDUALLY TO MAKE THE OUTPUT SMALLER
#evaluate()
printTree()
printExpr()


