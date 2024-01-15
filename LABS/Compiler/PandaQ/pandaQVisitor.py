# Generated from pandaQ.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .pandaQParser import pandaQParser
else:
    from pandaQParser import pandaQParser

# This class defines a complete generic visitor for a parse tree produced by pandaQParser.

class pandaQVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by pandaQParser#root.
    def visitRoot(self, ctx:pandaQParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#query.
    def visitQuery(self, ctx:pandaQParser.QueryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#selectExpr.
    def visitSelectExpr(self, ctx:pandaQParser.SelectExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderByExpr.
    def visitOrderByExpr(self, ctx:pandaQParser.OrderByExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#orderParamExpr.
    def visitOrderParamExpr(self, ctx:pandaQParser.OrderParamExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#whereExpr.
    def visitWhereExpr(self, ctx:pandaQParser.WhereExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#condicioParentesis.
    def visitCondicioParentesis(self, ctx:pandaQParser.CondicioParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#condicioAnd.
    def visitCondicioAnd(self, ctx:pandaQParser.CondicioAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#condicioOr.
    def visitCondicioOr(self, ctx:pandaQParser.CondicioOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#condicioSingle.
    def visitCondicioSingle(self, ctx:pandaQParser.CondicioSingleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#condicioExpr.
    def visitCondicioExpr(self, ctx:pandaQParser.CondicioExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#operadorBool.
    def visitOperadorBool(self, ctx:pandaQParser.OperadorBoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#allCamps.
    def visitAllCamps(self, ctx:pandaQParser.AllCampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#listCamps.
    def visitListCamps(self, ctx:pandaQParser.ListCampsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculatS.
    def visitCampCalculatS(self, ctx:pandaQParser.CampCalculatSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculatR.
    def visitCampCalculatR(self, ctx:pandaQParser.CampCalculatRContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculatM.
    def visitCampCalculatM(self, ctx:pandaQParser.CampCalculatMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculatD.
    def visitCampCalculatD(self, ctx:pandaQParser.CampCalculatDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campCalculatP.
    def visitCampCalculatP(self, ctx:pandaQParser.CampCalculatPContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#campNoCalculat.
    def visitCampNoCalculat(self, ctx:pandaQParser.CampNoCalculatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#parentesis.
    def visitParentesis(self, ctx:pandaQParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#div.
    def visitDiv(self, ctx:pandaQParser.DivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#suma.
    def visitSuma(self, ctx:pandaQParser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#numero.
    def visitNumero(self, ctx:pandaQParser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#pot.
    def visitPot(self, ctx:pandaQParser.PotContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#mul.
    def visitMul(self, ctx:pandaQParser.MulContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#resta.
    def visitResta(self, ctx:pandaQParser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#select.
    def visitSelect(self, ctx:pandaQParser.SelectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#from.
    def visitFrom(self, ctx:pandaQParser.FromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by pandaQParser#taula.
    def visitTaula(self, ctx:pandaQParser.TaulaContext):
        return self.visitChildren(ctx)



del pandaQParser