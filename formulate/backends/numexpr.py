# Licensed under a 3-clause BSD style license, see LICENSE.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import math

from ..identifiers import IDs, ConstantIDs
from ..parser import Operator, Function, Parser, Constant


__all__ = [
    'numexpr_parser',
]


config = [
    Operator(IDs.MINUS, '-', rhs_only=True),
    Operator(IDs.PLUS, '+', rhs_only=True),
    Operator(IDs.ADD, '+'),
    Operator(IDs.SUB, '-'),
    Operator(IDs.MUL, '*'),
    Operator(IDs.DIV, '/'),
    Operator(IDs.MOD, '%'),

    Operator(IDs.EQ, '=='),
    Operator(IDs.NEQ, '!='),
    Operator(IDs.GT, '>'),
    Operator(IDs.GTEQ, '>='),
    Operator(IDs.LT, '<'),
    Operator(IDs.LTEQ, '<='),

    Operator(IDs.AND, '&'),
    Operator(IDs.OR, '|'),
    Operator(IDs.XOR, '^'),
    Operator(IDs.NOT, '~', rhs_only=True),

    Function(IDs.SQRT, 'sqrt'),
    Function(IDs.ABS, 'abs'),
    Function(IDs.WHERE, 'where', 3),

    Function(IDs.LOG, 'log'),
    Function(IDs.LOG10, 'log10'),
    Function(IDs.LOG1p, 'log1p'),

    Function(IDs.EXP, 'exp'),
    Function(IDs.EXPM1, 'expm1'),

    Function(IDs.SIN, 'sin'),
    Function(IDs.ASIN, 'arcsin'),
    Function(IDs.COS, 'cos'),
    Function(IDs.ACOS, 'arccos'),
    Function(IDs.TAN, 'tan'),
    Function(IDs.ATAN, 'arctan'),
    Function(IDs.ATAN2, 'arctan2', 2),

    Function(IDs.SINH, 'sinh'),
    Function(IDs.ASINH, 'arcsinh'),
    Function(IDs.COSH, 'cosh'),
    Function(IDs.ACOSH, 'arccosh'),
    Function(IDs.TANH, 'tanh'),
    Function(IDs.ATANH, 'arctanh'),
]


constants = [
    Constant(ConstantIDs.TRUE, 'true'),
    Constant(ConstantIDs.FALSE, 'false'),

    Constant(ConstantIDs.SQRT2, math.sqrt(2)),
    Constant(ConstantIDs.E, math.e),
    Constant(ConstantIDs.PI, math.pi),
    Constant(ConstantIDs.INVPI, 1/math.pi),
    Constant(ConstantIDs.PIOVER2, math.pi/2),
    Constant(ConstantIDs.PIOVER4, math.pi/4),
    Constant(ConstantIDs.TAU, 2*math.pi),
    Constant(ConstantIDs.LN10, math.log(10)),
    Constant(ConstantIDs.LOG10E, math.log10(math.e)),
]


numexpr_parser = Parser('numexpr', config, constants)
