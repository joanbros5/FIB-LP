# Generated from AChurch.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,5,30,2,0,7,0,2,1,7,1,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        4,1,15,8,1,11,1,12,1,16,1,1,1,1,3,1,21,8,1,1,1,1,1,5,1,25,8,1,10,
        1,12,1,28,9,1,1,1,0,1,2,2,0,2,0,0,31,0,4,1,0,0,0,2,20,1,0,0,0,4,
        5,3,2,1,0,5,1,1,0,0,0,6,7,6,1,-1,0,7,21,5,4,0,0,8,9,5,1,0,0,9,10,
        3,2,1,0,10,11,5,2,0,0,11,21,1,0,0,0,12,14,5,5,0,0,13,15,5,4,0,0,
        14,13,1,0,0,0,15,16,1,0,0,0,16,14,1,0,0,0,16,17,1,0,0,0,17,18,1,
        0,0,0,18,19,5,3,0,0,19,21,3,2,1,2,20,6,1,0,0,0,20,8,1,0,0,0,20,12,
        1,0,0,0,21,26,1,0,0,0,22,23,10,1,0,0,23,25,3,2,1,2,24,22,1,0,0,0,
        25,28,1,0,0,0,26,24,1,0,0,0,26,27,1,0,0,0,27,3,1,0,0,0,28,26,1,0,
        0,0,3,16,20,26
    ]

class AChurchParser ( Parser ):

    grammarFileName = "AChurch.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "VAR", "LAMBDA" ]

    RULE_root = 0
    RULE_terme = 1

    ruleNames =  [ "root", "terme" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    VAR=4
    LAMBDA=5

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def terme(self):
            return self.getTypedRuleContext(AChurchParser.TermeContext,0)


        def getRuleIndex(self):
            return AChurchParser.RULE_root

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = AChurchParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.terme(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return AChurchParser.RULE_terme

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class VariableContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AChurchParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def VAR(self):
            return self.getToken(AChurchParser.VAR, 0)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariable" ):
                return visitor.visitVariable(self)
            else:
                return visitor.visitChildren(self)


    class AbstraccioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AChurchParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LAMBDA(self):
            return self.getToken(AChurchParser.LAMBDA, 0)
        def terme(self):
            return self.getTypedRuleContext(AChurchParser.TermeContext,0)

        def VAR(self, i:int=None):
            if i is None:
                return self.getTokens(AChurchParser.VAR)
            else:
                return self.getToken(AChurchParser.VAR, i)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAbstraccio" ):
                return visitor.visitAbstraccio(self)
            else:
                return visitor.visitChildren(self)


    class TermeParContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AChurchParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self):
            return self.getTypedRuleContext(AChurchParser.TermeContext,0)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermePar" ):
                return visitor.visitTermePar(self)
            else:
                return visitor.visitChildren(self)


    class AplicacioContext(TermeContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a AChurchParser.TermeContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def terme(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(AChurchParser.TermeContext)
            else:
                return self.getTypedRuleContext(AChurchParser.TermeContext,i)


        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAplicacio" ):
                return visitor.visitAplicacio(self)
            else:
                return visitor.visitChildren(self)



    def terme(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = AChurchParser.TermeContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_terme, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                localctx = AChurchParser.VariableContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 7
                self.match(AChurchParser.VAR)
                pass
            elif token in [1]:
                localctx = AChurchParser.TermeParContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 8
                self.match(AChurchParser.T__0)
                self.state = 9
                self.terme(0)
                self.state = 10
                self.match(AChurchParser.T__1)
                pass
            elif token in [5]:
                localctx = AChurchParser.AbstraccioContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 12
                self.match(AChurchParser.LAMBDA)
                self.state = 14 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 13
                    self.match(AChurchParser.VAR)
                    self.state = 16 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==4):
                        break

                self.state = 18
                self.match(AChurchParser.T__2)
                self.state = 19
                self.terme(2)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 26
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = AChurchParser.AplicacioContext(self, AChurchParser.TermeContext(self, _parentctx, _parentState))
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_terme)
                    self.state = 22
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 23
                    self.terme(2) 
                self.state = 28
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.terme_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def terme_sempred(self, localctx:TermeContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




