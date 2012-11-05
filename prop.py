#!/usr/bin/env python

# PropVar
# Connective


class PropVar(object):
    def __init__(self, value):
        self.value = value


    def evaluate(self):
        print "PV, my value is", self.value
        return self.value



class Not(object):
    def __init__(self, expr):
        self.expr = expr


    def evaluate(self):
        print "evaluating NOT"
        return not self.expr.evaluate()



class And(object):
    def __init__(self, e1, e2):
        self.e1 = e1
        self.e2 = e2


    def evaluate(self):
        print "evaluating AND"
        return self.e1.evaluate() and self.e2.evaluate()



p = PropVar(True)
q = PropVar(False)

# p ^ ~q
print And(p, Not(q)).evaluate()

"""
evaluating AND
PV, my value is True
evaluating NOT
PV, my value is False
True
"""


