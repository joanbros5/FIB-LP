# Generated from exprs.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .exprsParser import exprsParser
else:
    from exprsParser import exprsParser

# This class defines a complete generic visitor for a parse tree produced by exprsParser.

class exprsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by exprsParser#root.
    def visitRoot(self, ctx:exprsParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#function.
    def visitFunction(self, ctx:exprsParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#cap.
    def visitCap(self, ctx:exprsParser.CapContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#parametres.
    def visitParametres(self, ctx:exprsParser.ParametresContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#mainExp.
    def visitMainExp(self, ctx:exprsParser.MainExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#write.
    def visitWrite(self, ctx:exprsParser.WriteContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assignacio.
    def visitAssignacio(self, ctx:exprsParser.AssignacioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicional.
    def visitCondicional(self, ctx:exprsParser.CondicionalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#while.
    def visitWhile(self, ctx:exprsParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#returnInstr.
    def visitReturnInstr(self, ctx:exprsParser.ReturnInstrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#return.
    def visitReturn(self, ctx:exprsParser.ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#writeExp.
    def visitWriteExp(self, ctx:exprsParser.WriteExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#assigExp.
    def visitAssigExp(self, ctx:exprsParser.AssigExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condnalExp.
    def visitCondnalExp(self, ctx:exprsParser.CondnalExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#bucleExp.
    def visitBucleExp(self, ctx:exprsParser.BucleExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#condicioExp.
    def visitCondicioExp(self, ctx:exprsParser.CondicioExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#div.
    def visitDiv(self, ctx:exprsParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#suma.
    def visitSuma(self, ctx:exprsParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#numero.
    def visitNumero(self, ctx:exprsParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#pot.
    def visitPot(self, ctx:exprsParser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#mul.
    def visitMul(self, ctx:exprsParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#capFuncio.
    def visitCapFuncio(self, ctx:exprsParser.CapFuncioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#variable.
    def visitVariable(self, ctx:exprsParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#resta.
    def visitResta(self, ctx:exprsParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#eq.
    def visitEq(self, ctx:exprsParser.EqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#se.
    def visitSe(self, ctx:exprsParser.SeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#ge.
    def visitGe(self, ctx:exprsParser.GeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#st.
    def visitSt(self, ctx:exprsParser.StContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#gt.
    def visitGt(self, ctx:exprsParser.GtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by exprsParser#neq.
    def visitNeq(self, ctx:exprsParser.NeqContext):
        return self.visitChildren(ctx)



del exprsParser