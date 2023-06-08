# Generated from AChurch.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .AChurchParser import AChurchParser
else:
    from AChurchParser import AChurchParser

# This class defines a complete generic visitor for a parse tree produced by AChurchParser.

class AChurchVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by AChurchParser#root.
    def visitRoot(self, ctx:AChurchParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AChurchParser#variable.
    def visitVariable(self, ctx:AChurchParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AChurchParser#abstraccio.
    def visitAbstraccio(self, ctx:AChurchParser.AbstraccioContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AChurchParser#termePar.
    def visitTermePar(self, ctx:AChurchParser.TermeParContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by AChurchParser#aplicacio.
    def visitAplicacio(self, ctx:AChurchParser.AplicacioContext):
        return self.visitChildren(ctx)



del AChurchParser