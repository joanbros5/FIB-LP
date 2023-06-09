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
        4,0,5,21,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,1,
        1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,0,0,5,1,1,3,2,5,3,7,4,9,5,1,0,2,1,
        0,97,122,2,0,92,92,955,955,20,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,1,11,1,0,0,0,3,13,1,0,0,0,5,15,1,0,0,0,
        7,17,1,0,0,0,9,19,1,0,0,0,11,12,5,40,0,0,12,2,1,0,0,0,13,14,5,41,
        0,0,14,4,1,0,0,0,15,16,5,46,0,0,16,6,1,0,0,0,17,18,7,0,0,0,18,8,
        1,0,0,0,19,20,7,1,0,0,20,10,1,0,0,0,1,0,0
    ]

class AChurchLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    VAR = 4
    LAMBDA = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "VAR", "LAMBDA" ]

    ruleNames = [ "T__0", "T__1", "T__2", "VAR", "LAMBDA" ]

    grammarFileName = "AChurch.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


