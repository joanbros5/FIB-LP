# Generated from AChurch.g4 by ANTLR 4.13.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,1,7,6,-1,2,0,7,0,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,6,0,1,1,0,0,
        0,1,3,1,0,0,0,3,4,5,111,0,0,4,5,5,108,0,0,5,6,5,97,0,0,6,2,1,0,0,
        0,1,0,0
    ]

class achurchLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'ola'" ]

    symbolicNames = [ "<INVALID>",
 ]

    ruleNames = [ "T__0" ]

    grammarFileName = "AChurch.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


