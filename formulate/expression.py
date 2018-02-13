# Licensed under a 3-clause BSD style license, see LICENSE.
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from .identifiers import IDs


__all__ = [
    'Component',
    'Expression',
    'Variable',
]


class Component(object):
    def n_variables(self):
        raise NotImplementedError()

    # Binary arithmetic operators
    def __add__(self, value):
        return Expression(IDs.ADD, self, value)

    def __radd__(self, value):
        return Expression(IDs.ADD, value, self)

    def __sub__(self, value):
        return Expression(IDs.SUB, self, value)

    def __rsub__(self, value):
        return Expression(IDs.SUB, value, self)

    def __mul__(self, value):
        return Expression(IDs.MUL, self, value)

    def __rmul__(self, value):
        return Expression(IDs.MUL, value, self)

    def __truediv__(self, value):
        # TODO Is this correct for both Python 2 and 3?
        raise NotImplementedError()

    def __rtruediv__(self, value):
        # TODO Is this correct for both Python 2 and 3?
        raise NotImplementedError()

    def __floordiv__(self, value):
        # TODO Is this correct for both Python 2 and 3?
        raise NotImplementedError()

    def __rfloordiv__(self, value):
        # TODO Is this correct for both Python 2 and 3?
        raise NotImplementedError()

    def __abs__(self):
        return Expression(IDs.ABS, self)

    def __pow__(self, other, modulo=None):
        if modulo is None:
            return Expression(IDs.POW, self, other)
        else:
            # TODO Can we keep this optimisation in one operation?
            return Expression(IDs.MOD, Expression(IDs.POW, self, other), modulo)

    def __mod__(self, other):
        return Expression(IDs.MOD, self, other)

    def __and__(self, other):
        return Expression(IDs.AND, self, other)

    def __xor__(self, other):
        return Expression(IDs.XOR, self, other)

    def __or__(self, other):
        return Expression(IDs.OR, self, other)

    def __lshift__(self, other):
        return Expression(IDs.LSHIFT, self, other)

    def __rshift__(self, other):
        return Expression(IDs.RSHIFT, self, other)

    def __neg__(self):
        return Expression(IDs.MINUS, self)

    def __pos__(self):
        return Expression(IDs.PLUS, self)

    def __invert__(self):
        return Expression(IDs.NOT, self)

    def __complex__(self):
        raise NotImplementedError()

    def __int__(self):
        raise NotImplementedError()

    def __long__(self):
        raise NotImplementedError()

    def __float__(self):
        raise NotImplementedError()

    def __oct__(self):
        raise NotImplementedError()

    def __hex__(self):
        raise NotImplementedError()

    def __lt__(self, other):
        return Expression(IDs.LT, self, other)

    def __le__(self, other):
        return Expression(IDs.LTEQ, self, other)

    def __eq__(self, other):
        return Expression(IDs.EQ, self, other)

    def __ne__(self, other):
        return Expression(IDs.NEQ, self, other)

    def __ge__(self, other):
        return Expression(IDs.GTEQ, self, other)

    def __gt__(self, other):
        return Expression(IDs.GT, self, other)

    # Functions
    def where(self):
        raise NotImplementedError()

    def sin(self):
        return Expression(IDs.SIN, self)

    def cos(self):
        return Expression(IDs.COS, self)

    def tan(self):
        return Expression(IDs.TAN, self)

    def arcsin(self):
        return Expression(IDs.ASIN, self)

    def arccos(self):
        return Expression(IDs.ACOS, self)

    def arctan(self):
        return Expression(IDs.ATAN, self)

    def arctan2(self, other):
        return Expression(IDs.ATAN2, self, other)

    def sinh(self):
        return Expression(IDs.ASINH, self)

    def cosh(self):
        return Expression(IDs.COSH, self)

    def tanh(self):
        return Expression(IDs.TANH, self)

    def arcsinh(self):
        return Expression(IDs.ASINH, self)

    def arccosh(self):
        return Expression(IDs.ACOSH, self)

    def arctanh(self):
        return Expression(IDs.ATANH, self)

    def log(self):
        return Expression(IDs.LOG, self)

    def log10(self):
        return Expression(IDs.LOG10, self)

    def log1p(self):
        return Expression(IDs.LOG1p, self)

    def exp(self):
        return Expression(IDs.EXP, self)

    def expm1(self):
        return Expression(IDs.EXPM1, self)

    def sqrt(self):
        return Expression(IDs.SQRT, self)

    def abs(self):
        return Expression(IDs.ABS, self)

    def conj(self):
        raise NotImplementedError()

    def real(self):
        raise NotImplementedError()

    def imag(self):
        raise NotImplementedError()

    def complex(self):
        raise NotImplementedError()


class Expression(Component):
    def __init__(self, id, *args):
        self._id = id
        self._args = args

    def __repr__(self):
        return '{class_name}<{id_name}>({args})'.format(
            class_name=self.__class__.__name__, id_name=self.id.name,
            args=", ".join(map(repr, self.args)))

    def __str__(self):
        return repr(self)

    def equivilent(self, other):
        """Check if two expression objects are the same"""
        raise NotImplementedError()
        if isinstance(other, self.__class__):
            return self.id == other.id and self._args == other._args
        return False

    @property
    def id(self):
        return self._id

    @property
    def args(self):
        return self._args

    def to_string(self, config, constants):
        if self.id == IDs.CONST:
            assert len(self.args) == 1, self.args
            return constants[self.args[0]].to_string()
        else:
            return config[self.id].to_string(self, config, constants)


class Variable(Component):
    def __init__(self, name):
        self._name = name

    def __repr__(self):
        return '{class_name}({name})'.format(
            class_name=self.__class__.__name__, name=self.name)

    def __str__(self):
        return self.name

    @property
    def name(self):
        return self._name

    def to_string(self, config, constants):
        return self.name
